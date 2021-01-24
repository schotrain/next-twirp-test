from dotenv import load_dotenv
load_dotenv(dotenv_path='.env.local')

import os
import jwt
from twirp.asgi import TwirpASGIApp
from twirp import exceptions, errors
from generated import haberdasher_twirp, user_twirp
from services.haberdasher_impl import HaberdasherService
from services.user_impl import UserService
from services import constants

class CORSTwirpASGIApp(TwirpASGIApp):
    async def _respond(self, send, status, headers, body_bytes):
        headers["Access-Control-Allow-Origin"] = os.getenv("CORS_HOSTS")
        headers["Access-Control-Allow-Headers"] = "*"
        await super()._respond(send=send, status=status, headers=headers, body_bytes=body_bytes)


    def _with_middlewares(self, *args, func, ctx, request):
        if "authorization" in ctx.get("raw_headers"):
            auth_header = ctx.get("raw_headers")["authorization"]
            if not auth_header.lower().startswith("bearer "):
                raise exceptions.TwirpServerException(
                    code=errors.Errors.Unauthenticated,
                    message="Invalid authorization header"
                )
            auth_token = auth_header.split(" ")[1]
            try:
                auth_token_decoded = jwt.decode(auth_token, os.getenv("AUTH_SECRET"), algorithms=["HS512"])
                ctx.set(constants.AUTH_TOKEN_DECODED, auth_token_decoded)
            except:
                raise exceptions.TwirpServerException(
                    code=errors.Errors.Unauthenticated,
                    message="Invalid authorization token"
                )
        else:
            ctx.set(constants.AUTH_TOKEN_DECODED, None)
        
        return super()._with_middlewares(func=func, ctx=ctx, request=request)


    async def __call__(self, scope, receive, send):
        scope_type = scope['type']
        http_method = scope['method']
        if scope_type == 'http' and http_method == "OPTIONS":
            await self._respond(
                send=send,
                status=200,
                headers={},
                body_bytes=bytes()
            )
        else:
            await super().__call__(scope, receive, send)



app = CORSTwirpASGIApp()

haberdasherService = haberdasher_twirp.HaberdasherServer(service=HaberdasherService(), server_path_prefix="/rpc")
app.add_service(haberdasherService)

userService = user_twirp.UserServer(service=UserService(), server_path_prefix="/rpc")
app.add_service(userService)