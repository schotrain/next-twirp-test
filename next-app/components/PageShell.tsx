import { Alignment, Button, Menu, MenuItem, Navbar } from "@blueprintjs/core";
import { Popover2 } from "@blueprintjs/popover2";
import { useSession } from "next-auth/client";
import useTranslation from 'next-translate/useTranslation'
import Link from 'next/link'
import { signIn, signOut } from 'next-auth/client'
import RegisterCard from "./RegisterCard";


const PageShell = ({ children }): JSX.Element => {
  const [authSession, authLoading] = useSession();
  const { t, lang } = useTranslation('common')

  const signInMenu = <Menu>
    <MenuItem text={t('sign-in-with-google')} onClick={() => { signIn("google") }} />
    <MenuItem text={t('sign-in-with-okta')} onClick={() => { signIn("okta") }} />
  </Menu>

  const userMenu = <Menu>
    <MenuItem text={t('sign-out')} onClick={() => { signOut() }} />
  </Menu>

  return (
    <div className="bp3-dark">
      <Navbar fixedToTop={true}>
        <Navbar.Group align={Alignment.LEFT}>
          <Navbar.Heading><Link href="/">{t('title')}</Link></Navbar.Heading>
        </Navbar.Group>
        <Navbar.Group align={Alignment.RIGHT}>
          {authSession && <Popover2 content={userMenu} placement={"bottom-start"}>
            <Button icon="user" rightIcon="caret-down" text={authSession.rpcUser ? `${authSession.rpcUser.givenName} ${authSession.rpcUser.familyName}` : t('new-user')} />
          </Popover2>}
          {!authSession && <Popover2 content={signInMenu} placement={"bottom-start"}>
            <Button icon="user" rightIcon="caret-down" text={t('sign-in')} />
          </Popover2>}
        </Navbar.Group>
      </Navbar>
      <div className="body-content">
        {authSession && !authSession.rpcUser && <RegisterCard />}
        {children}
      </div>

      <style jsx>{`
            @import 'variables';
            .body-content {
                margin-top: $pt-navbar-height;
                padding: 10px;
            }
        `}</style>

      <style jsx global>{`
            body {
                background-color: #30404d;
                color: #f5f8fa;
            }
            *:focus {
              outline: 1px solid rgb(50, 50, 50);
            }
        `}</style>
    </div>
  )
}

export default PageShell