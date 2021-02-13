import os
import hmac
import hashlib
import jwt
import datetime
from data.models.user import IdentityProviderUser
from generated import user_pb2
from data import models, queries
from twirp import errors
from twirp.context import Context
from twirp.exceptions import InvalidArgument, TwirpServerException
from services import constants


class UserService(object):
    def getAccessToken(
        self, context: Context, getAccessTokenRequest: user_pb2.GetAccessTokenRequest
    ) -> user_pb2.GetAccessTokenResponse:
        if getAccessTokenRequest.identityProvider == None:
            raise InvalidArgument(
                argument="identityProvider", error="Invalid identity provider"
            )
        if getAccessTokenRequest.identityProviderId == None:
            raise InvalidArgument(
                argument="identityProviderId", error="Invalid identityProviderId"
            )
        if getAccessTokenRequest.hmac == None:
            raise InvalidArgument(argument="hmac", error="Invalid hmac")

        key = os.getenv("AUTH_SECRET")
        key_bytes = bytes(key, "UTF-8")
        message_bytes = bytes(
            str(getAccessTokenRequest.identityProvider)
            + getAccessTokenRequest.identityProviderId,
            "UTF-8",
        )
        computedHmac = hmac.new(key_bytes, message_bytes, hashlib.sha512).hexdigest()

        if computedHmac != getAccessTokenRequest.hmac:
            raise InvalidArgument(argument="hmac", error="Invalid hmac")

        jwt_body = {
            constants.IDENTITY_PROVIDER: user_pb2.IdentityProvider.Name(
                getAccessTokenRequest.identityProvider
            ),
            constants.IDENTITY_PROVIDER_ID: getAccessTokenRequest.identityProviderId,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
        }
        encoded_jwt = jwt.encode(jwt_body, os.getenv("AUTH_SECRET"), algorithm="HS512")

        return user_pb2.GetAccessTokenResponse(accessToken=encoded_jwt)

    def getUserInfo(
        self, context: Context, getUserInfoRequest: user_pb2.GetUserInfoRequest
    ) -> user_pb2.GetUserInfoResponse:

        decoded_access_token = context.get(constants.AUTH_TOKEN_DECODED)
        if not decoded_access_token:
            raise TwirpServerException(
                code=errors.Errors.Unauthenticated,
                message="Invalid authorization token",
            )

        idp_user = queries.get_user_from_idp_login(
            decoded_access_token[constants.IDENTITY_PROVIDER],
            decoded_access_token[constants.IDENTITY_PROVIDER_ID],
        )

        if idp_user:
            user_info = user_pb2.UserInfo(
                id=idp_user.user.id,
                email=idp_user.user.email,
                givenName=idp_user.user.givenName,
                familyName=idp_user.user.familyName,
                imageUrl=idp_user.user.imageUrl,
            )
        else:
            user_info = None

        return user_pb2.GetUserInfoResponse(userInfo=user_info)

    def saveUserInfo(
        self, context, saveUserInfoRequest: user_pb2.SaveUserInfoRequest
    ) -> user_pb2.SaveUserInfoRequest:
        decoded_access_token = context.get(constants.AUTH_TOKEN_DECODED)
        if not decoded_access_token:
            raise TwirpServerException(
                code=errors.Errors.Unauthenticated,
                message="Invalid authorization token",
            )

        idp_user = queries.get_user_from_idp_login(
            decoded_access_token[constants.IDENTITY_PROVIDER],
            decoded_access_token[constants.IDENTITY_PROVIDER_ID],
        )

        if not idp_user:
            idp_user = models.User(
                givenName=saveUserInfoRequest.givenName,
                familyName=saveUserInfoRequest.familyName,
                email=saveUserInfoRequest.email,
                identityProviderUsers=[
                    IdentityProviderUser(
                        provider=decoded_access_token[constants.IDENTITY_PROVIDER],
                        provider_id=decoded_access_token[
                            constants.IDENTITY_PROVIDER_ID
                        ],
                    )
                ],
            )
        else:
            idp_user.givenName = saveUserInfoRequest.givenName
            idp_user.familyName = saveUserInfoRequest.familyName
            idp_user.email = saveUserInfoRequest.email

        queries.save_user(idp_user)