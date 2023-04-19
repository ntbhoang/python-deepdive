"""
    1- a <= b if (a < b) or (a == b)
    2- a > b if not (a < b) and (a != b)
    3- a >= b if not (a < b)
"""


def complete_ordering(cls):
    if "__eq__" in dir(cls) and "__lt__" in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not (self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)

    return cls


from functools import total_ordering


@total_ordering
class Point:
    def __init__(self, *args):
        self.x, self.y = args

    def __abs__(self):
        from math import sqrt
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f"Point {self.x} - {self.y}"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented


p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 200)

print(p1 > p4)
print(p1 <= p2)
