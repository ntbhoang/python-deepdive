from functools import wraps


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function `{fn.__name__}`, which id = `{id(fn)}` was called {count} time(s).")

        return fn(*args, **kwargs)  # return the result of the original function

    return inner  # return the closure


def add(a: int, b: int):
    """

    :param a: integer
    :param b: integer
    :return: sum of a and b
    """

    return a + b


def mult(a: int, b: int, c: int = 1, *, d):
    """

   :param a:
   :param b:
   :param c:
   :param d:
   :return: Multiples of 4 values
   """

    return a * b * c * d


print(help(add))
print(id(add))

add = counter(add)  # decorate the `add` function

print(id(add))
print(help(add))

print(add(1, 2))

mult = counter(mult)  # decorate the `mult` function

result = mult(1, 2, 3, d=11)
print(f"Multiple result = {result}")


@counter
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b


print(divide(102, 4))
print(help(divide))
