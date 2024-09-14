import asyncio
from datetime import datetime
import random


class RCONServer:
    
    def __init__(self):
        self.rcon_loop = asyncio.get_event_loop()
    
    def dt(self):
        return datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    
    def build_rcon_functions(self):
        rcon_servers = []
        for server in ['game1','game2']:
            rcon_servers.append(
                self.rcon_command(server,
                                  "192.168.0.1",
                                  "30000",
                                  "some_password",
                                  random.randint(5, 10)
                                  )
            )
        
        return rcon_servers
    
    async def rcon_command(self, server: str, ip: str, port: str, passwd: str, interval: int):
        while True:
            await asyncio.sleep(int(interval))
            print(self.dt(), ">", server)
    
    async def run_loop(self):
        rcon_tasks = self.build_rcon_functions()
        try:
            print(self.dt(), "> Start")
            await asyncio.gather(*rcon_tasks)
            self.rcon_loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            print(self.dt(), "> End")
            self.rcon_loop.close()


obj = RCONServer()
asyncio.run(obj.run_loop())
