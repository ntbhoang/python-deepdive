from math import sqrt

a = 10, 20, 30, 99, 15

print(type(a))

# We want 1st and 2 last values, other we don't care
x, *_, y, z = a  # unpacking values

print(x)
print(y)
print(z)
print(_)


# Data Structure
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__} (x={self.x} , y={self.y})"


pt = Point2D(10, 20)
print(f"Before with original x value, x={pt.x}")
print(id(pt))
pt.x = 100
print(f"After with x value, x={pt.x}")
print(id(pt))

# declare a tuple
my_tuple = Point2D(11, 22), Point2D(22, 33)
print(type(my_tuple))

# be careful when using tuple, because what it contains maybe mutable
my_tuple[1].x = 55
print(my_tuple[1])

# modify a tuple
t1 = 1, 2, 3
t1 += (4, 5)
print(t1)  # remember this is a new tuple not the original one

# 4- data

london = "London", "UK", 8_700_000
new_york = "New York", "USA", 9_700_000
saigon = "Sai Gon", "Viet Nam", 12_000_000

cities = [london, new_york, saigon]  # list of tuple cities

# 4-1 extract the population only

total = sum(city[2] for city in cities)
print(total)

for item in enumerate(cities):
    print(item)

for idx, city in enumerate(cities):
    print(idx, city)

# 5-random


def random_shot(radius):

    from random import random, uniform
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False

    return  random_x, random_y, is_in_circle


attempts = 100
count_inside = 0
for i in range(attempts):
    *_, is_in_circle_ = random_shot(1)
    if is_in_circle_:
        count_inside += 1


print(f"Pi is approximately: {4 * count_inside / attempts}")



