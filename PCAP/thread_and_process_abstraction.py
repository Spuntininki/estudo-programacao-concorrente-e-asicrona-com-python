#from concurrent.futures.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor
import time


def processo():
    print('[', end='', flush=True)
    for _ in range(0, 10):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', flush=True)


if __name__ == '__main__':
    with Executor() as executor:
       future = executor.submit(processo)
    