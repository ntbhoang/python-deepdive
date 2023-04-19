def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args,**kwargs)
        print("{0}: called {1}".format(run_dt, fn.__name__))

        return result

    return inner


def dec_1(fn):
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        print(f"Running this {fn.__name__}")
        return fn(*args, **kwargs)

    return inner


@logged
@dec_1
def func_1():
    pass


@logged
@dec_1
def func_2():
    pass


func_2()
func_1()





