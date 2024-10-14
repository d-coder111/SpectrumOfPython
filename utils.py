import random

def random_direction():
    return random.choice(["horizontal", "vertical"])

def random_coordinate(size):
    return random.randint(0, size - 1)

def is_valid_coordinate(x, y, size):
    return 0 <= x < size and 0 <= y < size
