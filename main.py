import sys
from game.ship_battle import ShipBattle
from game.game_board import GameBoard
from ui.console_ui import ConsoleUI
from ui.gui_ui import GUIUI
from game.room import Room

def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == '-m':
        game_mode = 'multiplayer'
    else:
        game_mode = 'singleplayer'

    if game_mode == 'multiplayer':
        room_name = input('Enter room name: ')
        room = Room(room_name)
        room.start_game()
    else:
        game_logic = ShipBattle()
        if len(sys.argv) > 1 and sys.argv[1] == '-g':
            ui = GUIUI(game_logic)
        else:
            ui = ConsoleUI(game_logic)
        ui.play_game()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    game_board = GameBoard(10)
    ship_battle = ShipBattle(game_board)
    ship_battle.play_game()
    ship_battle.save_game('game.save')

    loaded_ship_battle = ShipBattle.load_game('game.save')
    loaded_ship_battle.play_game()
