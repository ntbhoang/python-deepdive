class Card:
    """
        - The sign of boilerplate pain:
            - There are only 2 attributes `rank` and `suit `, both repeated 3 time just for initialize the instance
        - For regular class, we have to override over dunder methods
    """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        if other.__class__ is not self.__class__: return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(rank= {self.rank!r}, suit= {self.suit!r})")


queen_of_hearts = Card("Q", "Hearts")
# queen_of_hearts_2 = Card("Q", "Heart")
# print(queen_of_hearts_2
#       == queen_of_hearts_1)
print(queen_of_hearts)
print(queen_of_hearts == Card("Q", "Hearts"))
# a queen of hearts is not the same as the queen of hearts

