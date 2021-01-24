import os
import hmac
import hashlib
import requests
import jwt
import datetime
from generated import user_pb2
from twirp.exceptions import InvalidArgument, TwirpServerException
from data.data import getDbSession
from data.models import User, IdentityProviderUser
from services import constants

class UserService(object):
    
    def getAccessToken(self, context, getAccessTokenRequest):
        if getAccessTokenRequest.identityProvider == None:
            raise InvalidArgument(argument="identityProvider", error="Invalid identity provider")
        if getAccessTokenRequest.identityProviderId == None:
            raise InvalidArgument(argument="identityProviderId", error="Invalid identityProviderId")
        if getAccessTokenRequest.hmac == None:
            raise InvalidArgument(argument="hmac", error="Invalid hmac")
        
        key = os.getenv("AUTH_SECRET")
        key_bytes = bytes(key, 'UTF-8')
        message_bytes = bytes(str(getAccessTokenRequest.identityProvider) + getAccessTokenRequest.identityProviderId, 'UTF-8')
        computedHmac = hmac.new(key_bytes, message_bytes, hashlib.sha512).hexdigest()

        if computedHmac != getAccessTokenRequest.hmac:
            raise InvalidArgument(argument="hmac", error="Invalid hmac")
        
        jwt_body = {
            "identityProvider":user_pb2.IdentityProvider.Name(getAccessTokenRequest.identityProvider), 
            "identityProviderId": getAccessTokenRequest.identityProviderId,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes = 10)
        }
        encoded_jwt = jwt.encode(jwt_body, os.getenv("AUTH_SECRET"), algorithm="HS512")

        return user_pb2.GetAccessTokenResponse(
            accessToken=encoded_jwt
        )
    

    def getUserInfo(self, context, getUserInfoRequest):
        decoded_access_token = context.get(constants.AUTH_TOKEN_DECODED)
        print(F"Decoded access token {decoded_access_token}")
        db_session = getDbSession()
        user = db_session.query(User).join(User.identityProviders).filter(IdentityProviderUser.provider == 'google').filter(IdentityProviderUser.provider_id == 'id').first()
        if user:
            userInfo = user_pb2.UserInfo(
                id=user.id,
                email = user.email,
                givenName = user.givenName,
                familyName = user.familyName,
                imageUrl = user.imageUrl
            )
        else:
            userInfo = None
        
        return user_pb2.GetUserInfoResponse(userInfo=userInfo)
