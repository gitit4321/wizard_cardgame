rank_map = {'je': 'Jester', 'j': 'Jack', 'q': 'Queen', 'k': 'King', 'a': 'Ace', 'w': 'Wizard'}
suit_map = {'clubs': 'Clubs', 'diams': 'Diamonds', 'spades': 'Spades', 'hearts': 'Hearts'}


class Card:

    def __init__(self, rank, suit=None):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        output = f"{self.__class__.__name__}({self.rank}"
        if self.suit is not None:
            output += f", {self.suit}"
        return output + ")"

    def __str__(self):
        output = f"{rank_map.get(self.rank, self.rank)}"
        if self.suit is not None:
            output += f" of {suit_map[self.suit]}"
        return output


if __name__ == "__main__":
    c1 = Card('j', 'clubs')
    c2 = Card('a', 'clubs')
    # c3 = Card('a', 'clubs')
    print(str(c1))
    print(repr(c1))
    print(str(c2))
    print(repr(c2))
    print(c1 == c2)
    print(c1 < c2)
    print(c1 > c2)
