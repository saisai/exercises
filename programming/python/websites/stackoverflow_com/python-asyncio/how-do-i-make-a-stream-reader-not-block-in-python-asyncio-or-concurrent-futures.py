
from asyncio import (
        Event,
        TimeoutError,
        create_task,
        gather,
        run,
        sleep,
        wait_for,
        )

async def loop(flag: Event):
    while True:
        try:
            await wait_for(flag.wait(), timeout=3)
        except TimeoutError:
            print("Took too long...")
        else:
            print("Someting happended!")
            flag.clear()

async def flag_setter(flag: Event):
    i = 0
    while True:
        print("Iteraint", i)
        if i % 5 == 0:
            flag.set()
        await sleep(1)
        i += 1

async def main():
    flag = Event()
    loop_task = create_task(loop(flag))
    setter_task = create_task(flag_setter(flag))
    await gather(loop_task, setter_task)

if __name__ == '__main__':
    try:
        run(main())
    except KeyboardInterrupt:
        print("\rStopped")


