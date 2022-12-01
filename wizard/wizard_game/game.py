from round import Round


class Game:
    def __init__(self, num_players=3):
        self.num_players = num_players
        self.round = 1
        self.total_rounds = 60 // self.num_players  # 60 cards in a standard Wizard deck
        self.score_card = {i: [] for i in range(self.num_players)}
        self.dealer = 0

    def play_round(self):
        round = Round(self.round, self.num_players)
        print(f"Played round {self.round}")


if __name__ == "__main__":
    g = Game(6)
    while g.round <= g.total_rounds:
        g.play_round(g.round)
        g.round += 1
    print(g.score_card)
