import random
import time

response = 'This should be kind of a long response that should be demonstrate how multiple coroutine cooperate to achive faster I/O' * 10  # NOQA
length = len(response)


def return_response(chunk_size=20):
    random_network_delay = round(random.randint(1, 9) * 0.001, 3)  # ms
    for i in range(0, length, chunk_size):
        time.sleep(random_network_delay)
        yield response[i:i + chunk_size]


def read(x):
    start = time.time()
    "".join([n for n in return_response()])
    stop = time.time()
    print(f'Function {x} took {stop-start} seconds to finish')


if __name__ == '__main__':
    start = time.time()
    for x in range(2, 50):
        read(x)

    stop = time.time()
    print(f'Total time: {stop - start}')
