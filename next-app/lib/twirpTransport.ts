import { TwirpFetchTransport } from '@protobuf-ts/twirp-transport'
import { RpcOptions, UnaryCall } from '@protobuf-ts/runtime-rpc'
import { HaberdasherClient } from '../generated/haberdasher'
import { UserClient } from '../generated/user';


export function getHaberdasherClient(authToken: string): HaberdasherClient {
  return new HaberdasherClient(getTwirpTransport(authToken));
}

export function getUserClient(): UserClient {
  return new UserClient(getTwirpTransport());
}

function getTwirpTransport(authToken?: string): TwirpFetchTransport {
  return new TwirpFetchTransport({
    baseUrl: process.env.NEXT_PUBLIC_TWIRP_ENDPOINT,
    sendJson: true,
    interceptors: [
      {
        // adds auth header to unary requests
        interceptUnary(next, method, input, options: RpcOptions): UnaryCall {
          if (!options.meta) {
            options.meta = {};
          }
          if (authToken) {
            options.meta['Authorization'] = authToken;
          }
          return next(method, input, options);
        }
      }
    ]
  })
}