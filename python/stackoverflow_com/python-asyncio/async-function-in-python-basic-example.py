import time
import asyncio
from datetime import datetime

async def do_some_iterations():
    for i in range(10):
        print(datetime.now().time())
        await asyncio.sleep(1)
    print("... Cool!")

async def do_something():
    print("Something...")
    for i in range(10):
        print("i ", i)
        #time.sleep(i)
        #await asyncio.sleep(i)

async def main():
    await asyncio.gather(
            do_some_iterations(),
            do_something()
            )

if __name__ == '__main__':
    asyncio.run(main())
    print('done')

    # https://stackoverflow.com/questions/73724271/async-function-in-python-basic-example
