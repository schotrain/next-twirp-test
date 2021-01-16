import uuid
import requests
from generated import user_pb2
from twirp.exceptions import InvalidArgument, TwirpServerException

class UserService(object):
    def _lookupGoogleIdentity(self, accessToken):
        identityServer = "https://www.googleapis.com/oauth2/v1/userinfo?alt=json"
        r = requests.get(identityServer, headers={'Authorization': 'Bearer ' + accessToken})
        if r.status_code != requests.codes.ok:
            return None
        jsonData = r.json()
        
        return {
            'givenName': jsonData["given_name"],
            'familyName': jsonData["family_name"],
            'email': jsonData["email"],
            'imageUrl': jsonData["picture"]
        }


    def _lookupOktaIdentity(self, accessToken):
        identityServer = "https://dev-9242554.okta.com/oauth2/v1/userinfo"
        r = requests.get(identityServer, headers={'Authorization': 'Bearer ' + accessToken})
        if r.status_code != requests.codes.ok:
            return None
        jsonData = r.json()

        return {
            'givenName': jsonData["given_name"],
            'familyName': jsonData["family_name"],
            'email': jsonData["email"],
            'imageUrl': ""
        }


    def TokenExchange(self, context, tokenExcangeRequest):
        if tokenExcangeRequest.identityProvider == None:
            raise InvalidArgument(argument="identityProvider", error="Invalid identity provider")
        if tokenExcangeRequest.idpAccessToken == None:
            raise InvalidArgument(argument="idpAccessToken", error="Invalid idpAccessToken")
        
        userData = None
        if tokenExcangeRequest.identityProvider == user_pb2.IdentityProvider.GOOGLE:
            userData = self._lookupGoogleIdentity(tokenExcangeRequest.idpAccessToken)
        if tokenExcangeRequest.identityProvider == user_pb2.IdentityProvider.OKTA:
            userData = self._lookupOktaIdentity(tokenExcangeRequest.idpAccessToken)

        if userData == None:
            raise TwirpServerException(code="UserLookup", message="Error lookup up user data")

        accessToken = str(uuid.uuid4())

        # TODO store this in a session db or redis or something

        return user_pb2.TokenExchangeResponse(
            userData=user_pb2.UserData(
                id="asdf",
                email=userData['email'],
                givenName=userData['givenName'],
                familyName=userData['familyName'],
                imageUrl=userData['imageUrl']
            ),
            accessToken=accessToken
        )
