from collections import namedtuple
"""
    1- For simple data structures, we can probably use tuple or dict
"""

"""
    2- It works. However, it puts a lot of responsibility on you as a programmer:
        - You need to remember that the `queen_of_hearts` var is represents a card.
        - For tuple version: 
            - You need to remember the order of the attributes.
            Writing ('Spades', 'A') will mess up your program but probably not give you an 
            easily understandable error message.
        - For dict version: you must makesure the names of the attributesare consistent.
        For example: {"value": "A", "suit": "Spades} will not work as expected.
"""

queen_of_hearts_tuple = ("Q", "Hearts")
queen_of_hearts_dict = {"rank": "Q", "suit": "Hearts"}

print(queen_of_hearts_tuple[0])
print(queen_of_hearts_dict["suit"])

"""
    3- NamedTuple:
        A better alternative is the namedtuple. It has long been used to create readable small data structures.
    - Why it seems like a good thing, this lack of awareness bout its own type can lead to subtle and hard to find bugs
    especially, when compare 2 different namedtuple classes.
    - Some restrictions:
        - Hard to add default values to some fields in a namedtuple.
        - A namedtuple is immutable, so the value of namedtuple can never be changed.
        In some applications, this is an awesome feature, but in other settings, it would be nice to have more 
        flexibility.
    - Data classes will not replace all uses of namedtuple. For instance, 
    if you need your data structure to behave like a tuple, then a named tuple is a great alternative!
"""

NamedTupleCard = namedtuple("NamedTupleCard", ["rank", "suit"])

queen_of_hearts = NamedTupleCard("Q", "Hearts")
print(queen_of_hearts.suit)


Person = namedtuple("Person", ["first_name", "last_name"])

ace_of_spades = NamedTupleCard("A", "Spades")

print(ace_of_spades == Person("A", "Spades"))   # True

card = NamedTupleCard("7", "Diamonds")
# card.rank = "9"   # AttributeError: can't set attribute
