import asyncio

async def delay(sec: int):
    print(f"dealy() going to sleep for {sec}s")
    await asyncio.sleep(sec)
    print("delay() waked up")

async def main():
    task =asyncio.create_task(delay(5))

    seconds_elapsed = 0
    while not task.done():
        print(f"checking task finished... {task.done()}")
        await asyncio.sleep(1)
        seconds_elapsed +=1
        if seconds_elapsed == 3:
            print(f"cancelled result: {task.cancel()}")
            print(f"task is done: {task.done()}")
        print(f"check task again: {task.done()}")

    print("main() awaiting task")
    try:
        #await task
        pass
    except asyncio.CancelledError:
        print("task was cancelled")
    print("main() finished")

asyncio.run(main())



# https://stackoverflow.com/questions/73804498/why-the-while-loop-on-asyncio-tasks-done-method-break-even-though-the-conditi

