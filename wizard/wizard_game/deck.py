from card import Card
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self.deck = []

        for i in range(4):
            for j in range(0, 15):
                if j == 0 or j == 14:
                    self.deck.append(Card(j))
                else:
                    self.deck.append(Card(j, i))

    def __str__(self):
        output = ""
        for card in self.deck:
            output += str(card) + '\n'
        return output

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


if __name__ == "__main__":
    d = Deck()
    print(d)
    d.shuffle()
    print(d)
