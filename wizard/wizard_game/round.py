from .exceptions import InvalidBidError, InvalidTrumpError
from .deck import Deck
from .hand import Hand
# from exceptions import InvalidBidError, InvalidTrumpError
# from deck import Deck
# from hand import Hand


class Round:
    def __init__(self, round: int, num_players: int, dealer: int) -> None:
        self.deck = Deck()
        self.num_players = num_players
        self.hand_size = round
        self.total_rounds = 60 // num_players
        self.player_hands = [Hand() for _ in range(num_players)]
        self.bids = [None] * num_players
        self.trump = None
        self.dealer = dealer
        self.turn = (dealer + 1) % num_players

    # deals player hands and sets trump suit, if any
    def deal_hands(self) -> None:
        self.deck.shuffle()

        # deal player hands
        for _ in range(self.hand_size):
            for i in range(self.num_players):
                player_hand = self.player_hands[i]
                card = self.deck.deal()
                player_hand.add_card(card)

    def dealer_set_trump(self) -> None:
        valid_selections = ['clubs', 'diamonds', 'spades', 'hearts']
        print(f"The flipped card is a Wizard. Since {self.dealer} is the dealer, they must select the trump suit for the current round.\n")

        while self.trump is None:
            # will need to change this to recieve user input from webpage
            selection = input(
                f"{self.dealer}, please select from the following (clubs, diamonds, spades, hearts): ")

            if selection.lower() not in valid_selections:
                raise InvalidTrumpError(f"InvalidTrumpError: You selected an invalid trump suit")
            else:
                if selection == 'diamonds':
                    self.trump = 'diams'
                self.trump = selection

    def set_trump(self):
        trump_card = self.deck.deal()
        self.trump = trump_card
        return trump_card

    def get_trump(self) -> None:
        # if not last round, flip top card to reveal trump suit
        if self.hand_size != self.total_rounds:
            card = self.deck.deal()

            # flipped card is a Wizard, so dealer picks trump suit
            if card.rank == 'w':
                self.dealer_set_trump()

            # flipped card is a Jester, so there is no trump suit
            elif card.rank == 'je':
                self.trump = None

            # set trump suit to that of the flipped card
            else:
                self.trump = card.suit

    def set_bid(self, player: int, bid: int) -> None:
        if 0 <= bid <= self.hand_size:
            self.bids[player] = bid
        else:
            raise InvalidBidError(f"InvalidBidError: Bid must be between 0 and {self.hand_size}")

    def get_user_bids(self) -> None:
        for i in range(self.num_players):
            while self.bids[i] is None:
                bid = int(input(f"Player {i}, select your bid: "))  # will need to change this to recieve user input from webpage
                try:
                    self.set_bid(i, bid)
                except InvalidBidError as error:
                    print(error)

    # def play_round(self) -> None:


if __name__ == "__main__":
    r = Round(3, 4, 0)
    r.deal_hands()
    # r.get_top_card()
    r.get_trump()
    # r.get_user_bids()
    # r.play_round()

    # r.set_bid(0, 2)
    # r.player_hands[0].sort()
    # print('poop')


# Need testing!!!
