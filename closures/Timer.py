import time
from time import perf_counter


class Timer:
    def __init__(self):
        self.start = perf_counter()

    # def pool(self):
    #     return perf_counter() - self.start

    # If we only have 1 call method, instead of calling that method, we can use the __call__

    def __call__(self):
        return perf_counter() - self.start


# t1 = Timer()
# time.sleep(4)
# print(t1.pool())


def stop_watch():
    start = perf_counter()

    def pool():
        nonlocal start
        return perf_counter() - start

    return pool


t2 = stop_watch()
time.sleep(4)
print(t2())