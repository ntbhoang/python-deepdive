

def outer():
    a = 100
    x = "python"

    def inner():
        a = 10  # local var
        print(f"{x} rocks")
        print(f"inner a = {a}")

    print(f"Outer a = {a}")
    return inner


# fn = outer()

# print(fn.__code__.co_freevars)  # print free var
# print(fn.__closure__)


"""Modifying a free var"""


def counter():
    count = 0

    def inc():
        nonlocal count
        count += 100
        return count

    return inc


f1 = counter()
f2 = counter()
print(f1())
print(f1())
print(f1())

# print(f1.__code__.co_freevars)  # print free var
# print(f1.__closure__)



