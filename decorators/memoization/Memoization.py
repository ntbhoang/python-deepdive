
# print(fib(3))


class Fib:

    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print(f"Calculating fib({n})")
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.cache[n]


f = Fib()

# print(f.fib(10))


def fib_closure():
    caches = {1: 1, 2: 1}

    def calc_fib(n):
        nonlocal caches
        if n not in caches:
            print(f"Calculating fib({n})")
            caches[n] = calc_fib(n - 1) + calc_fib(n - 2)
        return caches[n]

    return calc_fib


fc = fib_closure()
# print(fc(15))

# There is a trade-off when using cache, if we have a hundred thousands items in the cache
from functools import lru_cache


def memoize_fib(fib):
    caches = dict()

    def inner(n):
        if n not in caches:
            caches[n] = fib(n)
        return caches[n]

    return inner


@lru_cache(maxsize=16)
@memoize_fib
def fib(n):
    print(f"Calculating fib({n})")
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


print(fib(10))
