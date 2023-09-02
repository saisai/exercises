import asyncio
from websockets import connect

class TestClient:
    def __init__(self, URL):
        self.URL = URL
        self.conn = None
        self.loop = asyncio.get_event_loop()

    async def send(self, message):
        if self.conn == None:
            self.conn = await connect(self.URL)
        await self.conn.send(message)

    async def receive(self):
        return await self.conn.recv()

    def ping(self):
        return self.loop.run_until_complete(self._ping())

    async def _ping(self):
        await self.send("Hello World")
        return await self.receive()

test = TestClient("wss://echo.websocket.org")
print(test.ping())
