
a = 10


def func1():
    print(a)


def func2():
    a = 100
    print(a)


def func3():
    global a
    a = 101
    print(a)


print(f"before, the value of a = {a}")
func1()
func2()
func3()
print(f"After calling func3, the value of a = {a}")