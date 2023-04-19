from dataclasses import dataclass, field
from typing import List

"""
    1- Let's say that you want to give default values to the Deck.
    It would for example be convenient if Deck() created a regular (French) deck of 52 playing cards.
    First, specify the different ranks and suits. 
    Then, add a function make_french_deck() that creates a list of instances of PlayingCard:
    
    2- Don't introduce one of the most common anti-patterns in Python: using mutable default arguments.
    Let's say we add a list of cards as default value for Deck. The problem is that all instances of Deck will use 
    the same list objects as the default value of the cards prop. This mean that if 1 card is removed from one Deck
    then it disappears from all other instances as well.
    
    3- After setting order=True, instances of PlayingCard can be compared.
    
    4- For PlayingCard to use this sort index for comparisons,
    we need to add a field .sort_index to the class. 
    However, this field should be calculated from the other fields .rank and .suit automatically. 
    This is exactly what the special method .__post_init__() is for. 
    It allows for special processing after the regular .__init__() method is called:
    
    Note that .sort_index is added as the first field of the class. That way, the comparison is first 
    done using .sort_index and only if there are ties are the other fields used. Using field(), 
    you must also specify that .sort_index should not be included as a parameter in the 
    .__init__() method (because it is calculated from the .rank and .suit fields). 
    To avoid confusing the user about this implementation detail, it is probably also
     a good idea to remove .sort_index from the repr of the class.
"""

RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "♣ ♢ ♡ ♠".split()


def make_deck():
    return [Card(rank=r, suit=s) for r in RANKS for s in SUITS]


@dataclass(order=True)
class Card:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit))

    def __str__(self):
        return f"{self.rank}{self.suit}"


@dataclass
class Deck:
    # we want to  make 52 cards a default value when we ref to Deck.cards
    # Instead, data classes use something called a default_factory to handle mutable default values.
    # To use default_factory (and many other cool features of data classes), you need to use the field() specifier
    cards: list[Card] = field(default_factory=make_deck)

    def __repr__(self):
        cards = ",".join(f"{c!s}" for c in self.cards)
        return f"{self.__class__.__name__}({cards})"


queen_of_hearts = Card(rank="Q", suit="♡")
ace_of_spades = Card(rank="A", suit="♠")

deck1 = Deck()
print(sorted(make_deck()))

