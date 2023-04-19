
def outer_func():
    x = "hello"

    def inner_func():
        print(x)
    inner_func()


# outer_func()


def outer_f2():
    x = "hello"

    def inner():
        nonlocal x
        x = "python"
        print("inner: ", x)
    print("outer(before): ", x)
    inner()
    print("outer(after): ", x)

outer_f2()



