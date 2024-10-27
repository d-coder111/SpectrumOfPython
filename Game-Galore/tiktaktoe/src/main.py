import pygame
from utils import draw_board, check_winner, is_board_full

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 500  # Increased width and height for better centering
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
FONT = pygame.font.Font(None, 36)

# Game variables
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'
scores = {'X': 0, 'O': 0}
winning_line = None

# Reset button
RESET_BUTTON = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 60, 100, 40)

# Define draw_text function
def draw_text(text, x, y):
    surface = FONT.render(text, True, BLACK)
    SCREEN.blit(surface, (x, y))

def draw_winning_line(start, end):
    pygame.draw.line(SCREEN, RED, start, end, 5)

# Main game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over:
                x, y = event.pos
                board_x = (WIDTH - 300) // 2
                board_y = (HEIGHT - 300) // 2
                row, col = (y - board_y) // 100, (x - board_x) // 100
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '':
                    board[row][col] = current_player
                    if check_winner(board, current_player):
                        print(f"Player {current_player} wins!")
                        scores[current_player] += 1
                        game_over = True
                        winning_line = check_winner(board, current_player)
                    elif is_board_full(board):
                        print("It's a tie!")
                        game_over = True
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'
            
            if RESET_BUTTON.collidepoint(event.pos):
                board = [['' for _ in range(3)] for _ in range(3)]
                current_player = 'X'
                game_over = False
                winning_line = None

    SCREEN.fill(WHITE)
    
    # Draw turn text
    turn_text = f"Player {'1' if current_player == 'X' else '2'}'s Turn"
    draw_text(turn_text, 10, 10)
    
    # Draw scores
    draw_text(f"X: {scores['X']}  O: {scores['O']}", WIDTH // 2 - 50, 50)
    
    # Draw board
    draw_board(SCREEN, board, WIDTH, HEIGHT)
    
    # Draw winning line
    if winning_line:
        board_x = (WIDTH - 300) // 2
        board_y = (HEIGHT - 300) // 2
        start = (winning_line[1] * 100 + 50 + board_x, winning_line[0] * 100 + 50 + board_y)
        end = (winning_line[3] * 100 + 50 + board_x, winning_line[2] * 100 + 50 + board_y)
        draw_winning_line(start, end)
    
    # Draw reset button
    pygame.draw.rect(SCREEN, BLACK, RESET_BUTTON, 2)
    draw_text("Reset", RESET_BUTTON.x + 20, RESET_BUTTON.y + 10)
    
    pygame.display.flip()

pygame.quit()
