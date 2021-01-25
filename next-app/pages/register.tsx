import React from 'react'
import { signIn, signOut, useSession, } from 'next-auth/client'
import { Hat } from '../generated/haberdasher'
import { getHaberdasherClient } from '../rpc/twirpTransport'
import PageShell from '../components/PageShell'
import { Button } from '@blueprintjs/core'



export const Home = (): JSX.Element => {
  const [authSession, authLoading] = useSession();

  return (
    <>
      <PageShell>
        <div>
          Register
        </div>
      </PageShell>
    </>
  )
}

export default Home
