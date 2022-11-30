suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
values = ["Jester", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace", "Wizard"]


class Card:

    def __init__(self, val, suit=None):
        self.val = val
        self.suit = suit

    def __repr__(self):
        if self.suit or self.suit == 0:
            return f"{self.__class__.__name__} ({values[self.val]}, {suits[self.suit]}) : ({self.val}, {self.suit})"
        return f"{self.__class__.__name__} ({values[self.val]}) : ({self.val}, {self.suit})"

    def __str__(self):
        if self.suit or self.suit == 0:
            return f"{values[self.val]} of {suits[self.suit]}"
        return f"{values[self.val]}"

    def __eq__(self, other_obj):
        return self.val == other_obj.val

    def __lt__(self, other_obj):
        return self.val < other_obj.val


if __name__ == "__main__":
    c = Card(0)
    c2 = Card(14, 3)
    print(str(c))
    print(repr(c))
    print(str(c2))
    print(repr(c2))
    print(c == c2)
    print(c > c2)
