import asyncio
import functools

def set_event(event):
    print('setting event in callback')
    event.set()

async def coro1(event):
    print('coro1 wating for event')
    await event.wait()
    print('coror1 triggered')

async def coro2(event):
    print('coror2 waiting for event')
    await event.wait()
    print('coro2 tirggered')

async def main(loop):
    # create a shared event
    event = asyncio.Event()
    print('event start state: {}'.format(event.is_set()))

    loop.call_later(
        0.1, functools.partial(set_event, event)
    )

    #await asyncio.wait([coro1(event), coro2(event)])
    await asyncio.wait(
    [
        asyncio.create_task(coro1(event)),
        asyncio.create_task(coro2(event)),
    ]
    )

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
