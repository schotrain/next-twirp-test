import NextAuth from 'next-auth'
import Providers from 'next-auth/providers'
import { createHmac } from 'crypto'
import { getUserClient } from '../../../rpc/twirpTransport'
import { IdentityProvider } from '../../../generated/user'
import NodeCache from 'node-cache'

const accessTokenCache = new NodeCache({ stdTTL: 540 })

const getRpcAccessToken = async (identityProvider: string, identityProviderId: string): Promise<string> => {
    let reqIdentityProvider: IdentityProvider;
    if (identityProvider === 'google') reqIdentityProvider = IdentityProvider.GOOGLE;
    if (identityProvider === 'okta') reqIdentityProvider = IdentityProvider.OKTA;

    const cacheKey = reqIdentityProvider + identityProviderId;

    if (accessTokenCache.has(cacheKey)) {
        return accessTokenCache.get(cacheKey);
    }

    const secret = process.env.NEXTAUTH_SECRET;
    const hmac = createHmac('sha512', secret).update(cacheKey).digest('hex')

    const rpcCall = await getUserClient().getAccessToken({
        identityProvider: reqIdentityProvider,
        identityProviderId: identityProviderId,
        hmac: hmac
    })

    const accessToken = rpcCall.response.accessToken;
    accessTokenCache.set(cacheKey, accessToken);
    return accessToken
}

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
                token.identityProvider = account.provider;
                token.identityProviderId = account.id;
                token.givenName = profile.given_name;
                token.familyName = profile.family_name;
            }
            token.rpcAccessToken = await getRpcAccessToken(token.identityProvider, token.identityProviderId)
            return Promise.resolve(token)
        },
        // Custom logic that will pull values from our custom token into the session
        session: async (session, token) => {
            const sessionObj = {
                identityProviderUser: {
                    ...session.user,
                    givenName: token.givenName,
                    familyName: token.familyName
                },
                rpcAccessToken: token.rpcAccessToken,
                rpcUser: undefined
            }
            try {
                const getUserInfoResp = await getUserClient(token.rpcAccessToken).getUserInfo({})
                if (getUserInfoResp.response.userInfo) {
                    sessionObj.rpcUser = {
                        id: getUserInfoResp.response.userInfo.id,
                        email: getUserInfoResp.response.userInfo.email,
                        givenName: getUserInfoResp.response.userInfo.givenName,
                        familyName: getUserInfoResp.response.userInfo.familyName,
                        imageUrl: getUserInfoResp.response.userInfo.imageUrl
                    }
                }
            } catch (e) {
                console.error(e);
            }

            return Promise.resolve(sessionObj)
        }
    }
}

export default (req, res) => NextAuth(req, res, options)