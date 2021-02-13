import { Button, Card, Elevation, FormGroup, H4, InputGroup, Intent } from "@blueprintjs/core"
import { useSession } from "next-auth/client";
import useTranslation from "next-translate/useTranslation"
import { useState } from "react";
import { showToasterErrorMessage, showToasterSuscessMessage } from "../lib/toaster";
import { getUserClient } from "../rpc/twirpTransport";

const RegisterCard = (): JSX.Element => {
    const { t, lang } = useTranslation('common')
    const [authSession, authLoading] = useSession();

    const [givenName, setGivenName] = useState(authSession.identityProviderUser.givenName)
    const [familyName, setFamilyName] = useState(authSession.identityProviderUser.familyName)
    const [email, setEmail] = useState(authSession.identityProviderUser.email)
    const [imageUrl, setImageUrl] = useState(authSession.identityProviderUser.imageUrl)
    const [saving, setSaving] = useState(false)

    const saveUser = async () => {
        try {
            setSaving(true);
            const userClient = getUserClient(authSession.rpcAccessToken);
            await userClient.saveUserInfo({
                familyName,
                givenName,
                email,
                imageUrl
            })
            showToasterSuscessMessage(t('save-success'))
        } catch(ex) {
            showToasterErrorMessage(t('save-error'), ex)
        } finally {
            setSaving(false)
        }
    }

    return (
            <div className="register-card">
            <Card interactive={false} elevation={Elevation.ONE}>
                <H4>{t('register-new-user')}</H4>
                <p>{t('register-blurb')}</p>
                <FormGroup
                    label={t('given-name')}
                    labelFor="text-input"
                >
                    <InputGroup id="given-name" value={givenName} onChange={e => setGivenName(e.target.value)} />
                </FormGroup>
                <FormGroup
                    label={t('family-name')}
                    labelFor="text-input"
                >
                    <InputGroup id="family-name" value={familyName} onChange={e => setFamilyName(e.target.value)} />
                </FormGroup>
                <FormGroup
                    label={t('email')}
                    labelFor="text-input"
                >
                    <InputGroup id="email" value={email} onChange={e => setEmail(e.target.value)} />
                </FormGroup>
                <FormGroup
                    label={t('image-url')}
                    labelFor="text-input"
                >
                    <InputGroup id="image-url" value={imageUrl} onChange={e => setImageUrl(e.target.value)} />
                </FormGroup>

                <Button loading={saving} disabled={!givenName || !familyName || !email} onClick={saveUser}>{t('save')}</Button>
            </Card>
            <style jsx>{`
                .register-card {
                    margin-bottom: 20px;
                }
            `}</style>
        </div>
    )
}

export default RegisterCard