
import asyncio
from functools import partial

async def slow_function() -> int:
    await asyncio.sleep(5)
    return 100

class SomeClass:
    def __init__(self):
        self.slow_value = None

    def slow_function_wrapper(self) -> None:
        task = asyncio.create_task(slow_function()) # we do not wait anything here
        task.add_done_callback(partial(callback, obj=self))

def callback(fut: asyncio.Task, obj: SomeClass) -> None:
    if fut.exception():
        print("Error")
        obj.slow_value = -1
    else:
        print("Ok")
        obj.slow_value = fut.result()

async def result_pinger(obj: SomeClass) -> None:
    # we need to make asyncio loop busy with something
    while True:
        await asyncio.sleep(1)
        print(f"Result: {obj.slow_value}")
        if obj.slow_value is not None:
            break

async def main():
    x = SomeClass()
    x.slow_function_wrapper()
    await result_pinger(obj=x) # prevent asyncio loop from stopping

if __name__ == '__main__':
    #asyncio.run(main())
    '''
    while True:
        try:
            asyncio.run(main())
        except KeyboardInterrupt as e:
            print(e)
    '''
    # https://stackoverflow.com/questions/73727428/running-asyncio-task-without-await-causes-memory-issu

