from html import escape


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return f"{a} (<i>{str(hex(a))}</i>)"


def html_real(a):
    return f"{round(a, 2):.2f})"


def html_str(s):
    return html_escape(s).replace("\n", "<br/>\n")


def html_list(l):
    items = (f"<li>{html_escape(item)}</li>"
             for item in l)

    return "<ul>\n" + "\n".join(items) + "\n</ul>"


def html_dict(d):
    items = (f"<li>{k}={v}</li>"
             for k, v in d.items())

    return "<ul>\n" + "\n".join(items) + "\n</ul>"


def htmlize(arg):
    registry = {
        object: html_escape,
        int: html_int,
        str: html_str,
        list: html_list,
        dict: html_dict
    }  # dict

    # If the type of the arg is not exists in the registry, return the default is object
    fn = registry.get(type(arg), registry[object])

    return fn(arg)


print(htmlize(100))
print(htmlize("hello max and Rita"))
print(htmlize([1, "rocks"]))


def single_dispatch(fn):
    registry = {object: fn,
                int: lambda a: f"{a} (<i>{str(hex(a))}</i>)",
                str: lambda s: html_escape(s).replace("\n", "<br/>\n")
                }

    def inner(arg):
        return registry.get(type(arg), registry[object])(arg)

    return inner


@single_dispatch
def htmlize_decorator(a):
    return escape(str(a))


print(htmlize_decorator("1 < 100"))
