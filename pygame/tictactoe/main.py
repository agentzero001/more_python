import pygame as pg
#print(pg.__version__)

WIDTH, HEIGHT = 600, 600
LINE_COLOR = (80, 80, 80)
LINE_WIDTH = 5
GRID_SIZE = 3
X_COLOR = (90, 90, 90)
O_COLOR = (90, 90, 90)


board = [['' for _ in range(3)] for _ in range(3)]

turn = 'X'
game_over = False


pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic-Tac-Toe")

def draw_board():
    screen.fill((20, 20, 20))
    
    for x in range(1,3):
        
        pg.draw.line(screen, LINE_COLOR, (50, x*200), (WIDTH - 50, x*200), LINE_WIDTH)
        pg.draw.line(screen, LINE_COLOR, (x*200, 50), (x*200, WIDTH - 50), LINE_WIDTH)
 
    
    
CIRCLE_WIDTH = 15
CIRCLE_RADIUS = 60

    
def draw_XO():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                x = col * WIDTH // GRID_SIZE + WIDTH // (2 * GRID_SIZE)
                y = row * HEIGHT // GRID_SIZE + HEIGHT // (2 * GRID_SIZE)
                pg.draw.line(screen, X_COLOR, (x - CIRCLE_RADIUS, y - CIRCLE_RADIUS), (x + CIRCLE_RADIUS, y + CIRCLE_RADIUS), CIRCLE_WIDTH)
                pg.draw.line(screen, X_COLOR, (x - CIRCLE_RADIUS, y + CIRCLE_RADIUS), (x + CIRCLE_RADIUS, y - CIRCLE_RADIUS), CIRCLE_WIDTH)
            elif board[row][col] == 'O':
                x = col * WIDTH // GRID_SIZE + WIDTH // (2 * GRID_SIZE)
                y = row * HEIGHT // GRID_SIZE + HEIGHT // (2 * GRID_SIZE)
                pg.draw.circle(screen, O_COLOR, (x, y), CIRCLE_RADIUS, CIRCLE_WIDTH)



def check_win(player):
    # Check rows
    for row in range(GRID_SIZE):
        if all(board[row][col] == player for col in range(GRID_SIZE)):
            return True

    # Check columns
    for col in range(GRID_SIZE):
        if all(board[row][col] == player for row in range(GRID_SIZE)):
            return True

    # Check diagonals
    if (all(board[i][i] == player for i in range(GRID_SIZE)) or 
        all(board[i][GRID_SIZE - i - 1] == player for i in range(GRID_SIZE))):
        return True

    return False


player_turn = 'X'
running = True

while running:
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            running = False
    
        if event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())
            x, y = event.pos
            col = x // (WIDTH // GRID_SIZE) # e.g. 590 // 200 = 2
            row = y // (HEIGHT // GRID_SIZE)
            
            if board[row][col] == '':
                board[row][col] = player_turn
            
            
                player_turn = 'O' if player_turn == 'X' else 'X'
    
    
    draw_board()
    draw_XO()
        
    pg.display.update()


pg.math.Vector2()