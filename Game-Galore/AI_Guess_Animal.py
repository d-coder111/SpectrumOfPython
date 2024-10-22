import json
import os

class AnimalGame:
    def __init__(self):
        # Load animal data from a JSON file or create a default one if it doesn't exist
        self.folder_name = 'Game-Galore'
        self.data_file = os.path.join(self.folder_name, 'animals.json')
        self.animals = self.load_data()

    def load_data(self):
        """Load animal data from a JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                'questions': {},
                'animals': ['dog', 'cat', 'elephant', 'tiger', 'lion', 'rabbit', 'fish']
            }

    def save_data(self):
        """Save animal data to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.animals, file)

    def play_game(self):
        print("Think of an animal, and I will try to guess it!")
        self.ask_question('Is it a mammal?', 'mammal')

    def ask_question(self, question, key):
        """Ask a question and navigate through the game."""
        answer = input(f"{question} (yes/no): ").strip().lower()
        
        if answer == 'yes':
            if key in self.animals['questions']:
                next_question = self.animals['questions'][key]
                self.ask_question(next_question, key)
            else:
                animal = input("What animal did you think of? ")
                self.animals['questions'][key] = input("What question would distinguish this animal? ")
                self.animals['animals'].append(animal)
                self.save_data()
                print(f"Got it! I'll remember that a {animal} is a {key}.")
        elif answer == 'no':
            print("I couldn't guess it. Can you help me learn?")
            new_animal = input("What was the animal? ")
            new_question = input(f"What question would distinguish a {new_animal} from a {key}? ")
            self.animals['questions'][key] = new_question
            self.animals['animals'].append(new_animal)
            self.save_data()
            print(f"Thanks! I'll remember that a {new_animal} is different from a {key}.")

if __name__ == "__main__":
    game = AnimalGame()
    game.play_game()






# Game Instructions:

# 1.) Think of an animal.

# 2.) The AI will ask you yes/no questions to guess the animal.
 
# 3.) If the AI can't guess it, you can teach it by providing the name of the animal and a distinguishing question.

# 4.) The AI learns from your inputs and will improve its guessing ability over time.


# Data Storage:

# The game stores the questions and animals in a animals.json file. The first time you run the game, it will create this file with default data.






