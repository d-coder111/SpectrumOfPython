import pygame

def draw_board(screen, board, screen_width, screen_height):
    # Colors
    BLACK = (0, 0, 0)
    
    # Calculate board size and position
    BOARD_SIZE = 300
    x_offset = (screen_width - BOARD_SIZE) // 2
    y_offset = (screen_height - BOARD_SIZE) // 2
    
    # Draw the grid lines
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i * 100 + x_offset, y_offset), (i * 100 + x_offset, BOARD_SIZE + y_offset), 2)
        pygame.draw.line(screen, BLACK, (x_offset, i * 100 + y_offset), (BOARD_SIZE + x_offset, i * 100 + y_offset), 2)
    
    # Draw X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLACK, (col * 100 + 20 + x_offset, row * 100 + 20 + y_offset), 
                                 (col * 100 + 80 + x_offset, row * 100 + 80 + y_offset), 2)
                pygame.draw.line(screen, BLACK, (col * 100 + 80 + x_offset, row * 100 + 20 + y_offset), 
                                 (col * 100 + 20 + x_offset, row * 100 + 80 + y_offset), 2)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (col * 100 + 50 + x_offset, row * 100 + 50 + y_offset), 40, 2)


def check_winner(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return (i, 0, i, 2)
    
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return (0, i, 2, i)
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return (0, 0, 2, 2)
    if board[0][2] == board[1][1] == board[2][0] == player:
        return (0, 2, 2, 0)
    
    return None

def is_board_full(board):
    return all(cell != '' for row in board for cell in row)
