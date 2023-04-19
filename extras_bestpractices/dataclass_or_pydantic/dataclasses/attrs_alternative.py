"""
    1- Another alternative, and one of the inspiration for data classes, is the attrs project
    2- This can be used in exactly the same way as the DataClassCard and NamedTupleCard examples earlier.
    The attrs project is great and does support some features that data classes do not,
    including converters and validators.
    3- Furthermore, attrs has been around for a while and is supported in Python 2.7 as well as Python 3.4 and up.
    However, as attrs is not a part of the standard library, it does add an external dependency to your projects.
    Through data classes, similar functionality will be available everywhere.

"""
import attr


@attr.s
class AttrCard:
    rank = attr.ib()
    suit = attr.ib()


@attr.define
class Coordinates:
    x: int
    y: int


a1 = AttrCard("Queen", "Hearts")
print(a1)

c1 = Coordinates(x=10, y=11)
print(c1)
print(c1.x)
print(c1.y)


# If you want to initialize your private attributes yourself, you can do that too:
# If you prefer to expose your privates, you can use keyword argument aliases:
@attr.define
class PrivateCoordinates:
    _x: int = attr.field(init=False, default=42, alias="_x", kw_only=True)


pc1 = PrivateCoordinates()
print(pc1._x)
