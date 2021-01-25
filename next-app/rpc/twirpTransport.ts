import { TwirpFetchTransport } from '@protobuf-ts/twirp-transport'
import { RpcOptions, UnaryCall } from '@protobuf-ts/runtime-rpc'
import { HaberdasherClient } from '../generated/haberdasher'
import { UserClient } from '../generated/user';


export function getHaberdasherClient(authToken?: string): HaberdasherClient {
  return new HaberdasherClient(getTwirpTransport(authToken));
}

export function getUserClient(authToken?: string): UserClient {
  return new UserClient(getTwirpTransport(authToken));
}

function getTwirpTransport(authToken?: string): TwirpFetchTransport {
  return new TwirpFetchTransport({
    baseUrl: process.env.NEXT_PUBLIC_TWIRP_ENDPOINT,
    useProtoMethodName: true,
    sendJson: true,
    interceptors: [
      {
        // adds auth header to unary requests
        interceptUnary(next, method, input, options: RpcOptions): UnaryCall {
          if (!options.meta) {
            options.meta = {};
          }
          if (authToken) {
            options.meta['Authorization'] = `Bearer ${authToken}`;
          }
          return next(method, input, options);
        }
      }
    ]
  })
}