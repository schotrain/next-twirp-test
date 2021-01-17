import os
import hmac
import hashlib
import requests
import uuid
from generated import user_pb2
from twirp.exceptions import InvalidArgument, TwirpServerException

class UserService(object):
    
    def GetAccessToken(self, context, getAccessTokenRequest):
        if getAccessTokenRequest.identityProvider == None:
            raise InvalidArgument(argument="identityProvider", error="Invalid identity provider")
        if getAccessTokenRequest.identityProviderId == None:
            raise InvalidArgument(argument="identityProviderId", error="Invalid identityProviderId")
        if getAccessTokenRequest.hmac == None:
            raise InvalidArgument(argument="hmac", error="Invalid hmac")
        
        
        keyBytes = bytes(os.getenv("AUTH_SECRET"), 'UTF-8')
        messageBytes = bytes(str(getAccessTokenRequest.identityProvider) + getAccessTokenRequest.identityProviderId, 'UTF-8')
        computedHmac = hmac.new(keyBytes, messageBytes, hashlib.sha512).hexdigest()

        if computedHmac != getAccessTokenRequest.hmac:
            raise InvalidArgument(argument="hmac", error="Invalid hmac")
        
        accessToken = str(uuid.uuid4())

        return user_pb2.GetAccessTokenResponse(
            accessToken=accessToken
        )
    

    def GetUserInfo(self, context, getUserInfoRequest):
        return user_pb2.GetUserInfoResponse(
            userInfo=user_pb2.UserInfo(
                id="12345",
                email = 'me@you.com',
                givenName = 'given',
                familyName = 'family',
                imageUrl = 'http://www.test.com/image'
            )
        )
