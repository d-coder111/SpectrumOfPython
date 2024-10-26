from ship import Ship
import random

class Board:
    def __init__(self):
        self.size = 10
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.ships = []
        self.ship_counts = {
            1: 4,
            2: 3,
            3: 2,
            4: 1
        }
        self.shots_taken = set()

    def place_ship(self, ship, start_row, start_col, orientation):
        if self.can_place_ship(ship, start_row, start_col, orientation):
            ship.place(start_row, start_col, orientation)
            self.ships.append(ship)
            for position in ship.positions:
                row, col = position
                self.grid[row][col] = 1
            print(f"Placed ship of length {ship.length} at {start_row}, {start_col} in {orientation} orientation.")
        else:
            print(f"Cannot place ship of length {ship.length} at {start_row}, {start_col} in {orientation} orientation.")
            raise ValueError("Cannot place ship here!")

    def can_place_ship(self, ship, row, col, orientation):
        if orientation == 'horizontal':
            if col + ship.length > self.size:
                return False
            return all(self.grid[row][col + i] == 0 for i in range(ship.length))
        elif orientation == 'vertical':
            if row + ship.length > self.size:
                return False
            return all(self.grid[row + i][col] == 0 for i in range(ship.length))
        return False

    def receive_shot(self, row, col):
        print(f"Received shot at ({row}, {col})")
        self.shots_taken.add((row, col))
        if self.grid[row][col] == 1:
            for ship in self.ships:
                if self.is_hit(ship, row, col):
                    ship.hit((row, col))
                    self.grid[row][col] = 2
                    if ship.is_sunk():
                        print(f"Ship sunk at {ship.positions}!")
                    return True
        self.grid[row][col] = -1
        print("Miss!")
        return False

    def is_hit(self, ship, row, col):
        return (row, col) in ship.positions

    def check_all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)

    def display(self, reveal=False):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == 1 and not reveal:
                    print('0', end=' ')
                elif self.grid[row][col] == -1:
                    print('M', end=' ')
                else:
                    print(self.grid[row][col], end=' ')
            print()

    def setup_ships(self):
        self.ships = []
        for length, count in self.ship_counts.items():
            for _ in range(count):
                ship = Ship(length)
                placed = False
                while not placed:
                    start_row = random.randint(0, self.size - 1)
                    start_col = random.randint(0, self.size - 1)
                    orientation = random.choice(['horizontal', 'vertical'])
                    try:
                        self.place_ship(ship, start_row, start_col, orientation)
                        placed = True
                    except ValueError:
                        continue

    def is_location_shot(self, row, col):
        return (row, col) in self.shots_taken
