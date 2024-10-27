# Pygame Tic-Tac-Toe

## Introduction

This is a simple implementation of the classic Tic-Tac-Toe game using Python and Pygame. The game features a graphical user interface where two players can take turns placing their marks (X or O) on a 3x3 grid. The game includes a score tracker, a reset button, and a winning line animation.

Key features:
- Graphical user interface using Pygame
- Two-player gameplay
- Score tracking for both players
- Reset button to start a new game
- Winning line animation
- Centered game board

## Setup Instructions

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. Clone this repository or download the source code.

2. Install Pygame if you haven't already:
   ```
   pip install pygame
   ```

### Running the Game

1. Navigate to the project directory:
   ```
   cd path/to/tictactoe
   ```
2. Install the required packages:
   ```
   pip install pygame
   ```
3. Run the main script:
   ```
   python src/main.py
   ```

## How to Play

1. The game starts with Player 1 (X) and alternates to Player 2 (O).
2. Click on an empty cell to place your mark.
3. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the round.
4. The score is updated after each round.
5. Click the "Reset" button to start a new game while keeping the scores.

## Project Structure

- `src/main.py`: The main game loop and UI logic
- `src/utils.py`: Utility functions for game mechanics
- `README.md`: This file, containing project information and instructions

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](https://opensource.org/licenses/MIT)

