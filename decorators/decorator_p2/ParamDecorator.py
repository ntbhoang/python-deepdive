def dec_factory(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0

            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)

            avg = total_elapsed / reps
            print(f"Average run time {avg} , {reps} reps")

            return result

        return inner

    return timed


def memoize(fn):
    caches = dict()

    def caching(n):
        caches[n] = fn(n)

        return caches[n]

    return caching


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n - 1) + calc_fib_recurse(n - 2)


@memoize
@dec_factory(5)
def fib(n):
    return calc_fib_recurse(n)


print(fib(20))

