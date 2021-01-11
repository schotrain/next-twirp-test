import random

from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

from generated import haberdasher_twirp, haberdasher_pb2

class HaberdasherService(object):
    def MakeHat(self, context, size):
        if size.inches <= 0:
            raise InvalidArgument(argument="inches", error="I can't make a hat that small!")
        return haberdasher_pb2.Hat(
            inches=size.inches,
            color= random.choice(["white", "black", "brown", "red", "blue"]),
            name=random.choice(["bowler", "baseball cap", "top hat", "derby"])
        )



class CORSTwirpASGIApp(TwirpASGIApp):
    async def _respond(self, send, status, headers, body_bytes):
        headers["Access-Control-Allow-Origin"] = "*"
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


# if you are using a custom prefix, then pass it as `server_path_prefix`
# param to `HaberdasherServer` class.
service = haberdasher_twirp.HaberdasherServer(service=HaberdasherService())
app = CORSTwirpASGIApp()
app.add_service(service)