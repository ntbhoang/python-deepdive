def dec_factory(a, b):
    print("Running the dec_factory")

    def dec(fn):
        print("Running the dec")

        def inner(*args, **kwargs):
            print("Running inner")
            print(f"a={a}, b={b}")
            return fn(*args, **kwargs)

        return inner

    return dec


@dec_factory(3, 5)
def my_func():
    print("running my_func")


print(my_func())
