"""
    Python is a dynamic language, it means that we can modify class's instances at run time
"""

"""
    Application-1: Add debugging info into class
"""

from datetime import datetime, timezone


def info(self):
    results = [f"time: {datetime.now(timezone.utc)}", f"Class: {self.__class__.__name__}", f"id: {hex(id(self))}"]
    for k, v in vars(self).items():
        results.append(f"{k}: {v}")

    return results


def debug_info(cls):
    cls.debug = info
    return cls


@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @staticmethod
    def say_hi():
        return "Hello there!!"


@debug_info
class Automobile:
    def __init__(self, made, model, year, top_speed):
        self.made = made
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    def __str__(self):
        return f"Maker= {self.made}, model= {self.model}"

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError("Speed cannot exceed top_speed")
        else:
            self._speed = new_speed


p1 = Person("Max", 1985)
print(p1.debug())


a1 = Automobile(made="Tesla", model="TS450", year="2023", top_speed=150)
a1.speed = 140
print(a1.debug())





