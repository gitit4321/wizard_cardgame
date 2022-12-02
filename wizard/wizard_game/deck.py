from .card import Card
# from card import Card
from random import shuffle


suits = ["clubs", "diams", "spades", "hearts"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]


class Deck:

    def __init__(self) -> None:
        self.deck = []

        # standard 52 card deck
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

        # addition of 4 jesters ('je') and 4 wizards ('w')
        for _ in range(4):
            self.deck.append(Card('je'))
            self.deck.append(Card('w'))

    def __str__(self):
        output = ""
        for card in self.deck:
            output += str(card) + '\n'
        return output

    def __len__(self):
        return len(self.deck)

    def __iter__(self):
        i = 0
        while i < len(self.deck):
            yield self.deck[i]
            i += 1

    def __getitem__(self, i):
        return self.deck[i]

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        if len(self.deck) > 0:
            return self.deck.pop()


if __name__ == "__main__":
    from card import Card
    d = Deck()
    print(d)
