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
    jwt: {
        encode: async ({ secret, token, maxAge }) => { 
            const signingOptions = {algorithm: 'HS512'} as any
            delete token.exp
            signingOptions.expiresIn = maxAge
            return jwt.sign(token, secret, signingOptions)
        },
        decode: async ({ secret, token, maxAge }) => { 
            return jwt.verify(token, secret)
        }
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
        jwt: async (token, user, account, profile, isNewUser) => {
            const isSignIn = (user) ? true : false
            if (isSignIn) {
                let identityProvider: IdentityProvider;
                if (account.provider === 'google') identityProvider = IdentityProvider.GOOGLE;
                if (account.provider === 'okta') identityProvider = IdentityProvider.OKTA;

                const loginData = await getUserClient().login({
                    identityProvider,
                    accessToken: account.accessToken
                })
                token.userId = loginData.response.userData.id;
                token.email = loginData.response.userData.email;
                token.given_name = loginData.response.userData.givenName;
                token.family_name = loginData.response.userData.familyName;
                token.imageUrl = loginData.response.userData.imageUrl;
            } 
            return Promise.resolve(token)
        },
        session: async (session, user) => {
            delete session.user.image
            session.user.id = user.userId;
            session.user.email = user.email;
            session.user.given_name = user.given_name;
            session.user.family_name = user.family_name;
            session.user.imageUrl = user.imageUrl;
            return Promise.resolve(session)
        }
    }
}

export default (req, res) => NextAuth(req, res, options)