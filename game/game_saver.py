import json

class GameSaver:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_game(self, game_state):
        with open(self.file_path, 'w') as f:
            json.dump(game_state, f)

    def load_game(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)
