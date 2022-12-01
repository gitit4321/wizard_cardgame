from functools import cmp_to_key
from card import Card

# used by 'compare_cards' method to sort a given Hand
suits = [None, "clubs", "diams", "spades", "hearts"]
ranks = ["je", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a", "w"]


class Hand:
    def __init__(self) -> None:
        self.hand = []

    def add_card(self, card: Card) -> None:
        self.hand.append(card)

    def play_card(self, card: Card) -> Card:
        pass

    def compare_cards(self, card1: Card, card2: Card) -> int:
        rank1, suit1 = card1.rank, card1.suit
        rank2, suit2 = card2.rank, card2.suit

        if suits.index(suit1) == suits.index(suit2):
            if ranks.index(rank1) < ranks.index(rank2):
                return -1
            else:
                return 1
        if suits.index(suit1) < suits.index(suit2):
            return -1
        else:
            return 1

    def sort(self):
        self.hand.sort(key=cmp_to_key(self.compare_cards))


if __name__ == '__main__':
    h = Hand()
