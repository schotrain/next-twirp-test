import NextAuth from 'next-auth'
import Providers from 'next-auth/providers'
import jwt from 'jsonwebtoken'
import { getUserClient } from '../../../lib/twirpTransport'
import { IdentityProvider } from '../../../generated/user'

const options = {
    secret: process.env.NEXTAUTH_SECRET,
    session: {
        jwt: true
    },
    providers: [
        Providers.Okta({
            clientId: process.env.AUTH_OKTA_CLIENTID,
            clientSecret: process.env.AUTH_OKTA_CLIENTSECRET,
            domain: process.env.AUTH_OKTA_DOMAIN
        }),
        Providers.Google({
            clientId: process.env.AUTH_GOOGLE_CLIENTID,
            clientSecret: process.env.AUTH_GOOGLE_CLIENTSECRET
        }),
    ],
    callbacks: {
        // Custom logic that will exchange the IDP access token for an API server access token during login
        jwt: async (token, user, account, profile, isNewUser) => {
            const isSignIn = (user) ? true : false
            if (isSignIn) {
                let identityProvider: IdentityProvider;
                if (account.provider === 'google') identityProvider = IdentityProvider.GOOGLE;
                if (account.provider === 'okta') identityProvider = IdentityProvider.OKTA;

                const loginData = await getUserClient().tokenExchange({
                    identityProvider,
                    idpAccessToken: account.accessToken
                })
                token.userId = loginData.response.userData.id;
                token.email = loginData.response.userData.email;
                token.given_name = loginData.response.userData.givenName;
                token.family_name = loginData.response.userData.familyName;
                token.imageUrl = loginData.response.userData.imageUrl;
                token.rpcAccessToken = loginData.response.accessToken
            } 
            return Promise.resolve(token)
        },
        // Custom logic that will pull values from our custom token into the session
        session: async (session, user) => {
            delete session.user.image
            session.user.id = user.userId;
            session.user.email = user.email;
            session.user.given_name = user.given_name;
            session.user.family_name = user.family_name;
            session.user.imageUrl = user.imageUrl;
            session.rpcAccessToken = user.rpcAccessToken
            return Promise.resolve(session)
        }
    }
}

export default (req, res) => NextAuth(req, res, options)