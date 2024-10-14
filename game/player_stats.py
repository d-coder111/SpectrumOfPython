class PlayerStats:
    def __init__(self):
        self.wins = 0
        self.losses = 0

    def update_score(self, winner):
        if winner == 'X':
            self.wins += 1
        else:
            self.losses += 1

    def display_stats(self):
        print(f"Win: {self.wins}")
        print(f"Lose: {self.losses}")
