import NextAuth from 'next-auth'
import Providers from 'next-auth/providers'

const options = {
    secret: process.env.NEXTAUTH_SECRET,
    session: {
        jwt: true
    },
    jwt: {
        signingKey: process.env.NEXTAUTH_JWT_SIGNING_KEY
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
                token.idp = account.provider;
                token.idp_id = account.id;
                token.given_name = profile.given_name;
                token.family_name = profile.family_name;
            }
            return Promise.resolve(token)
        },
        session: async (session, user) => {
            session.user.idp = user.idp;
            session.user.idp_id = user.idp_id;
            session.user.given_name = user.given_name;
            session.user.family_name = user.family_name;
            return Promise.resolve(session)
        }
    }
}

export default (req, res) => NextAuth(req, res, options)