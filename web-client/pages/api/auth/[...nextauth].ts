import NextAuth from 'next-auth'
import Providers from 'next-auth/providers'

const options = {
    secret: process.env.NEXTAUTH_SECRET,
    session: {
        jwt: true
    },
    jwt: {
        secret: process.env.NEXTAUTH_SECRET
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
                token.idp_id= account.id;
                token.given_name = profile.given_name;
                token.family_name = profile.family_name;
             }
            return Promise.resolve(token)
        }
    }
}

export default (req, res) => NextAuth(req, res, options)