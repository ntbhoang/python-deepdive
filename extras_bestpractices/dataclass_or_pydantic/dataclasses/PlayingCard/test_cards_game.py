RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "♣ ♢ ♡ ♠".split()


print(RANKS.index("5") * len(SUITS) + SUITS.index("♡"))