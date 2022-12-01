class Card:

    def __init__(self, rank, suit=None):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        if self.suit is None:
            return f"{self.__class__.__name__} ({self.rank})"
        return f"{self.__class__.__name__} ({self.rank}, {self.suit})"

    def __str__(self):
        if self.suit is None:
            return f"{self.rank}"
        return f"{self.rank} of {self.suit}"

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
