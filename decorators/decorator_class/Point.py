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

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self):
        pass


p1 = Point(10, 20)
p2 = Point(20, 10)

print(abs(p1))
print(p1)
print(p1 is p2)