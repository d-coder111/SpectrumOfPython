class Ship:
    def __init__(self, length):
        self.length = length
        self.hits = 0
        self.positions = []

    def hit(self, position):
        self.hits += 1
        print(f"Ship hit at position {position}!")

    def is_sunk(self):
        return self.hits >= self.length

    def place(self, start_row, start_col, orientation):
        self.positions.clear()
        for i in range(self.length):
            if orientation == 'horizontal':
                self.positions.append((start_row, start_col + i))
            elif orientation == 'vertical':
                self.positions.append((start_row + i, start_col))

    def __str__(self):
        return f"Ship(length={self.length}, hits={self.hits}, positions={self.positions})"
