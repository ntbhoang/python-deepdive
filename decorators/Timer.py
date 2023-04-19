def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed_time = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f"{k} = {v}" for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ",".join(all_args)

        print("{0} ({1}) took {2:.6f}s to run.".format(fn.__name__,
                                                       args_str,
                                                       elapsed_time))

        return result

    return inner


# with recursive function we have a lot of extra calculations -> not efficient


@timed
def fibonacci_recursion(n: int) -> float:
    if n <= 2:
        return 1
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


# print(fibonacci_recursion(7))

@timed
def fib_recursion(n: int) -> float:
    return fibonacci_recursion(n)


@timed
def fib_loop_others(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n + 1):
        temp = fib_2
        fib_2 = fib_1 + fib_2
        fib_1 = temp

    return fib_2


@timed
def fib_loop_python(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return fib_2


@timed
def fib_reduce(n: int) -> int:
    from functools import reduce

    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0])
                   , dummy
                   , initial)
    return fib_n[0]


print(fib_loop_python(100))
print(fib_reduce(100))