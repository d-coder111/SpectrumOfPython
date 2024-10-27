import json
import random
from board import Board
from player import HumanPlayer, AIPlayer
from ship import Ship

class Game:
    def __init__(self):
        opponent_choice = input("Do you want to play against AI or another player? (AI/player): ")
        if opponent_choice.lower() == "ai":
            self.ai_player = AIPlayer("AI")
            self.human_player = HumanPlayer()
            self.board1 = Board()
            self.board2 = Board()
            self.board1.setup_ships()
            self.ai_setup_ships()
        else:
            self.human_player = HumanPlayer()
            self.second_player = HumanPlayer()
            self.board1 = Board()
            self.board2 = Board()
            self.board1.setup_ships()
            self.board2.setup_ships()

        self.current_player = self.human_player
        self.is_game_over = False
        self.shots_taken = set()

    def ai_setup_ships(self):
        ships_to_place = [Ship(1) for _ in range(4)] + [Ship(2) for _ in range(3)] + [Ship(3) for _ in range(2)] + [Ship(4) for _ in range(1)]
        
        for ship in ships_to_place:
            placed = False
            while not placed:
                try:
                    start_row = random.randint(0, self.board2.size - 1)
                    start_col = random.randint(0, self.board2.size - 1)
                    orientation = random.choice(['horizontal', 'vertical'])
                    self.board2.place_ship(ship, start_row, start_col, orientation)
                    placed = True
                except ValueError:
                    continue

    def shoot(self, row, col):
        if (row, col) in self.shots_taken:
            print("You have already shot at this position!")
            return False
        self.shots_taken.add((row, col))

        target_board = self.board2 if self.current_player == self.human_player else self.board1

        print(f"Player {self.current_player.name} is shooting at ({row}, {col})")
        hit = target_board.receive_shot(row, col)
        if hit:
            print("Hit!")
        else:
            print("Miss!")
    
        self.check_game_over()
        return hit

    def check_game_over(self):
        if self.board2.check_all_ships_sunk():
            self.is_game_over = True
            print(f"{self.current_player.name} wins!")
            self.ask_to_play_again()

    def ask_to_play_again(self):
        choice = input("Want to play again? (yes/no): ")
        if choice.lower() == 'yes':
            self.reset_game()
        else:
            print("Thanks for playing!")

    def reset_game(self):
        self.board1 = Board()
        self.board2 = Board()
        self.current_player = self.human_player
        self.is_game_over = False
        
        opponent_choice = input("Do you want to play against AI or another player? (AI/player): ")
        if opponent_choice.lower() == "ai":
            self.ai_player = AIPlayer("AI")
            self.board1.setup_ships()
            self.ai_setup_ships()
        else:
            self.second_player = HumanPlayer()
            self.board1.setup_ships()
            self.board2.setup_ships()

    def save_game(self, filename):
        game_state = {
            'board1': self.board1.grid,
            'board2': self.board2.grid,
            'current_player': self.current_player.name,
            'is_game_over': self.is_game_over
        }
        with open(filename, 'w') as f:
            json.dump(game_state, f)

    def load_game(self, filename):
        with open(filename, 'r') as f:
            game_state = json.load(f)
            self.board1.grid = game_state['board1']
            self.board2.grid = game_state['board2']
            self.current_player = self.human_player if game_state['current_player'] == self.human_player.name else self.ai_player
            self.is_game_over = game_state['is_game_over']

    def display_boards(self):
        print("Your Board:")
        self.board1.display(reveal=True)
        print("\nOpponent's Board (Hidden view):")
        self.board2.display()

    def play(self):
        while not self.is_game_over:
            print(f"Current player: {self.current_player.name}")
            self.display_boards()
        
            if self.current_player.is_ai:
                row, col = self.current_player.get_move()
                print(f"AI chose coordinates: ({row}, {col})")
            else:
                command = input("Enter 'save' to save or 'load' to load the game, or make a move (row col): ")
                if command.lower() == 'save':
                    self.save_game('game_save.json')
                    print("Game saved.")
                    continue
                elif command.lower() == 'load':
                    self.load_game('game_save.json')
                    print("Game loaded.")
                    continue
            
                try:
                    row, col = map(int, command.split())
                except ValueError:
                    print("Invalid input. Please enter coordinates in 'row col' format.")
                    continue

            hit = self.shoot(row, col)
            if not hit:
                self.current_player = self.ai_player if self.current_player == self.human_player else self.human_player

if __name__ == "__main__":
    game = Game()
    game.play()
