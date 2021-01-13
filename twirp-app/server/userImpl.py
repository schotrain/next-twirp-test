from generated import user_pb2
from twirp.exceptions import InvalidArgument, TwirpServerException

class UserService(object):
    def _lookupGoogleIdentity(self, accessToken):
        # TODO implement this. Probably move it as well to an identity provider package
        print("Looking up google data " + accessToken)
        return {
            'givenName': 'FirstG',
            'familyName': 'LastG',
            'email': 'test@google.com',
            'imageUrl': 'www.google.com/image'
        }

    def _lookupOktaIdentity(self, accessToken):
        # TODO implement this. Probably move it as well to an identity provider package
        print("Looking up okta data " + accessToken)
        return {
            'givenName': 'FirstO',
            'familyName': 'LastO',
            'email': 'test@okta.com',
            'imageUrl': 'www.okta.com/image'
        }

    def Login(self, context, loginRequest):
        #TODO document and test this. Also encrypt a key for future API calls
        if loginRequest.identityProvider == None:
            raise InvalidArgument(argument="identityProvider", error="Invalid identity provider")
        if loginRequest.accessToken == None:
            raise InvalidArgument(argument="accessToken", error="Invalid accessToken")
        
        userData = None
        if loginRequest.identityProvider == user_pb2.IdentityProvider.GOOGLE:
            userData = self._lookupGoogleIdentity(loginRequest.accessToken)
        if loginRequest.identityProvider == user_pb2.IdentityProvider.OKTA:
            userData = self._lookupOktaIdentity(loginRequest.accessToken)

        if userData == None:
            raise TwirpServerException(code="UserLookup", message="Error lookup up user data")

        return user_pb2.LoginResponse(
            userData=user_pb2.UserData(
                id="asdf",
                email=userData['email'],
                givenName=userData['givenName'],
                familyName=userData['familyName'],
                imageUrl=userData['imageUrl']
            )
        )
