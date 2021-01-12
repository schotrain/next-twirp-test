import os
from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument
from generated import haberdasher_pb2, haberdasher_twirp
from dotenv import load_dotenv
from server.haberdasherImpl import HaberdasherService

load_dotenv(dotenv_path='.env.local')

class CORSTwirpASGIApp(TwirpASGIApp):
    async def _respond(self, send, status, headers, body_bytes):
        headers["Access-Control-Allow-Origin"] = os.getenv("CORS_HOSTS")
        headers["Access-Control-Allow-Headers"] = "*"
        await super()._respond(send=send, status=status, headers=headers, body_bytes=body_bytes)

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


service = haberdasher_twirp.HaberdasherServer(service=HaberdasherService(), server_path_prefix="/rpc")
app = CORSTwirpASGIApp()
app.add_service(service)