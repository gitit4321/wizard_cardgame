from deck import Deck
from hand import Hand


class Round:
    def __init__(self, round, num_players):
        self.num_players = num_players
        self.hand_size = round
        self.total_rounds = 60 // num_players
        self.player_hands = [Hand() for _ in range(self.num_players)]
        self.trump = None
        self.bids = []
        self.tricks = []
        self.scores = []

    def deal_round(self):
        deck = Deck()
        deck.shuffle()

        # deal player hands
        for _ in range(self.hand_size):
            for i in range(self.num_players):
                player_hand = self.player_hands[i]
                card = deck.deal()
                player_hand.add_card(card)

        # if not last round, flip top card to reveal trump suit
        if self.hand_size != self.total_rounds:
            self.trump = deck.deal().suit


if __name__ == "__main__":
    r = Round(20, 3)
    r.deal_round()
    r.player_hands[0].sort()
    print('poop')
