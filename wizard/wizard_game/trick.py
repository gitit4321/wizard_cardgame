from card import Card


class Trick:
    def __init__(self, suit_lead, trump=None):
        self.trick = []
        self.suit_lead = suit_lead
        self.trump = trump

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def play_card(self, card: Card):
        pass
