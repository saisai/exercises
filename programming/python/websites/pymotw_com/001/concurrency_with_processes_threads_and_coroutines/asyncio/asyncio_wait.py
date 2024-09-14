import asyncio

async def phase(i):
    print('in phase {}'.format(i))
    await asyncio.sleep(0.1 * 1)
    print("done with phase {}".format(i))
    return 'phase {} resunt '.format(i)

async def main(num_phases):
    print('starting main')
    phases = [
            asyncio.create_task(phase(i))
            for i in range(num_phases)
            ]
    print('waiting for phases to complete')
    print('phases ', phases)
    completed, pending = await asyncio.wait(phases)
    results = [t.result() for t in completed]
    print('results: {!r}'.format(results))

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()
