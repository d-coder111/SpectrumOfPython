Little documentation for project

Sea_battle/ # Game project file
Sea_battle/ai_py # AI logic for the game
Sea_battle/battleship.py # The main file of the game through which it is launched
Sea_battle/board.py # Representation of logic and implementation of the playing field
Sea_battle/client.py # Client part of the game
Sea_battle/game_save.json # Location where the save is stored
Sea_battle/game.py # Game state management (including saves and save loads)
Sea_battle/player.py # The player's representation of both himself and an AI opponent/second real player.
Sea_battle/server.py # Server part of the game
Sea_battle/ship.py # Ship Logic View

How to run?: Through the terminal in VS Code and/or PyCharm, enter the command "cd C:\Users\Your_name\Desktop\Your_file\SpectrumOfPython\Game-Galore\Sea_battle", then in terminal write "python battleship.py".

How to play: First, select an opponent (AI or a real player, whom you are currently playing), then choose your (and second player, when you play against real man) nickname and game is generated 10x10 field with 4 types of ships. 4 one-cell ships, 3 two-cell ships, 2 three-cell ships and 1 four-cell ship. Your task is to sink all enemy ships while preserving your own. The round goes until victory. You will have to select the field for defeat using numbers from 0 to 9 in a column and line, the enemy bot/player does the same.

In the future, the game will be updated and released on mobile, joystick and computer controls, and graphics and sound will also be developed.

Now... have fun!