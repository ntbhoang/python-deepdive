def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value

    return inc


counter1 = counter()

print(counter1())


def counter_v1(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f"function `{fn.__name__}`, has been call {cnt} time(s)")
        return fn(*args, **kwargs)

    return inner


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


cnt_add = counter_v1(add)
print(cnt_add.__closure__)

cnt_add(10, 30)
cnt_add(10, 30)
cnt_add(10, 30)

print(cnt_add(10, 20))

counters = dict()


def counter_v2(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt  # assign key to value
        return fn(*args, **kwargs)

    return inner


counted_add = counter_v2(add)
counted_mult = counter_v2(mult)

print(counted_add(10, 11))
print(counted_add(10, 12))
print(counters)

"""last version"""


def counter_v3(fn, ctns: dict):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        ctns[fn.__name__] = cnt  # assign key to value
        return fn(*args, **kwargs)

    return inner


c = dict()
counted_add = counter_v3(add, c)
print(counted_add(1, 2))
print(counted_add(1, 3))
print(counted_add(1, 4))
print(c)
