import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
WHITE = (50, 50, 50)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (239, 47, 47)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_COLOR = (0, 0, 0)
CROSS_WIDTH = 15
GRID_SIZE = 3

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize the grid
grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Function to draw the grid
def draw_grid():
    for x in range(1, GRID_SIZE):
        pygame.draw.rect(screen, LINE_COLOR, (0, x * HEIGHT // GRID_SIZE, WIDTH, LINE_WIDTH))
        pygame.draw.rect(screen, LINE_COLOR, (x * WIDTH // GRID_SIZE, 0, LINE_WIDTH, HEIGHT))

# Function to draw the X's and O's
def draw_XO():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 'X':
                x = col * WIDTH // GRID_SIZE + WIDTH // (2 * GRID_SIZE)
                y = row * HEIGHT // GRID_SIZE + HEIGHT // (2 * GRID_SIZE)
                pygame.draw.line(screen, CROSS_COLOR, (x - CIRCLE_RADIUS, y - CIRCLE_RADIUS), (x + CIRCLE_RADIUS, y + CIRCLE_RADIUS), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (x - CIRCLE_RADIUS, y + CIRCLE_RADIUS), (x + CIRCLE_RADIUS, y - CIRCLE_RADIUS), CROSS_WIDTH)
            elif grid[row][col] == 'O':
                x = col * WIDTH // GRID_SIZE + WIDTH // (2 * GRID_SIZE)
                y = row * HEIGHT // GRID_SIZE + HEIGHT // (2 * GRID_SIZE)
                pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), CIRCLE_RADIUS, CIRCLE_WIDTH)

# Function to check for a win
def check_win(player):
    # Check rows
    for row in range(GRID_SIZE):
        if all(grid[row][col] == player for col in range(GRID_SIZE)):
            return True

    # Check columns
    for col in range(GRID_SIZE):
        if all(grid[row][col] == player for row in range(GRID_SIZE)):
            return True

    # Check diagonals
    if all(grid[i][i] == player for i in range(GRID_SIZE)) or all(grid[i][GRID_SIZE - i - 1] == player for i in range(GRID_SIZE)):
        return True

    return False

# Function to check for a tie
def check_tie():
    return all(grid[row][col] != '' for row in range(GRID_SIZE) for col in range(GRID_SIZE))

# Main game loop
player_turn = 'X'
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            col = x // (WIDTH // GRID_SIZE)
            row = y // (HEIGHT // GRID_SIZE)

            if grid[row][col] == '':
                grid[row][col] = player_turn
                                
                if check_win(player_turn):
                    game_over = True
                elif check_tie():
                    game_over = True

                player_turn = 'O' if player_turn == 'X' else 'X'

    screen.fill(WHITE)
    draw_grid()
    draw_XO()
    pygame.display.update()
