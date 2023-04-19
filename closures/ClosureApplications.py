
""" Normally we would create a class like this"""

class Average:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        return sum(self.numbers) / len(self.numbers)


a = Average()

a.add(10)
a.add(11)
a.add(12)
a.add(13)

b = Average()
b.add(10)


"""In this case, we can replace class with closure for simplicity """


def average():
    numbers = []

    def add(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)

    return add


c = average()
print(c(91))
print(c(1))
print(c(7))


def average_f1():
    total = 0
    count = 0

    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        return total / count

    return add


f2 = average_f1()
print(f2(0))
print(f2(4))
print(f2(5))

