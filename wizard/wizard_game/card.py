rank_map = {'je': 'Jester', 'j': 'Jack', 'q': 'Queen', 'k': 'King', 'a': 'Ace', 'w': 'Wizard'}
suit_map = {'clubs': 'Clubs', 'diams': 'Diamonds', 'spades': 'Spades', 'hearts': 'Hearts'}


class Card:

    def __init__(self, rank, suit=None):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        if self.suit is None:
            return f"{self.__class__.__name__} ({self.rank})"
        return f"{self.__class__.__name__} ({self.rank}, {self.suit})"

    def __str__(self):
        output = f"{rank_map.get(self.rank, self.rank)}"
        if self.suit is not None:
            output += f" of {suit_map[self.suit]}"
        return output

    # def __eq__(self, other_obj):
    #     return self.rank == other_obj.rank

    # def __lt__(self, other_obj):
    #     return self.rank < other_obj.rank


if __name__ == "__main__":
    c = Card(0)
    c2 = Card(14, 3)
    print(str(c))
    print(repr(c))
    print(str(c2))
    print(repr(c2))
    print(c == c2)
    print(c > c2)
