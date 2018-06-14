import asyncio
import random
import time

response = 'This should be kind of a long response that should be demonstrate how multiple coroutine cooperate to achive faster I/O' * 10  # NOQA
length = len(response)


async def return_response(chunk_size=20):
    random_network_delay = round(random.randint(1, 9) * 0.001, 3)  # ms
    for i in range(0, length, chunk_size):
        await asyncio.sleep(random_network_delay)
        yield response[i:i + chunk_size]


async def read(x):
    start = time.time()
    "".join([n async for n in return_response()])
    stop = time.time()
    print(f'Coroutine {x} took {stop-start} seconds to finish')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(read(x)) for x in range(2, 50)]
    start = time.time()
    loop.run_until_complete(asyncio.gather(*tasks))
    stop = time.time()
    loop.close()
    print(f'Total time: {stop - start}')
