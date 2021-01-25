import { Provider } from 'next-auth/client'
import "@blueprintjs/icons/lib/css/blueprint-icons.css"
import "@blueprintjs/popover2/lib/css/blueprint-popover2.css"
import "@blueprintjs/core/lib/css/blueprint.css"

function MyApp({ Component, pageProps }) {
  return (
    <Provider session={pageProps.session}>
      <Component {...pageProps} />
    </Provider>
  )
}

export default MyApp