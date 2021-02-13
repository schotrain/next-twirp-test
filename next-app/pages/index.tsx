import React from 'react'
import { signIn, signOut, useSession, } from 'next-auth/client'
import { Hat } from '../generated/haberdasher'
import { getHaberdasherClient } from '../rpc/twirpTransport'
import PageShell from '../components/PageShell'
import { Button } from '@blueprintjs/core'



export const Home = (): JSX.Element => {
  const [authSession, authLoading] = useSession();

  const callTwirp = async function () {
    const client = getHaberdasherClient();
    const call = await client.makeHat({ inches: 23 });
    const response: Hat = call.response;
    return response;
  }

  return (
    <>
      <PageShell>
        <div>
          <Button onClick={async () => {alert(JSON.stringify(await callTwirp()))}}>Call Twirp</Button>
        </div>
      </PageShell>
    </>
  )
}

export default Home
