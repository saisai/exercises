import asyncio

async def test():
    while True:
        print("test")
        await asyncio.sleep(7)

async def print_main():
    another_task = None
    while True:
        print("main")
        if another_task is None:
            another_task = asyncio.create_task(test())
        await asyncio.sleep(5)

def main():
    loop = asyncio.get_event_loop()
    loop.create_task(print_main())
    loop.run_forever()


if __name__ == '__main__':
    main()
