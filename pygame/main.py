import pygame as pg
#print(pg.__version__)

WIDTH, HEIGHT = 600, 600
LINE_COLOR = (80, 80, 80)
LINE_WIDTH = 5
GRID_SIZE = WIDTH // 3
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)


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
        
        

    # pg.draw.line(screen, LINE_COLOR, (200, 50), (200, 550), LINE_WIDTH)
    # pg.draw.line(screen, LINE_COLOR, (400, 50), (400, 550), LINE_WIDTH)
     
    # pg.draw.line(screen, LINE_COLOR, (50, 200), (550, 200), LINE_WIDTH)
    # pg.draw.line(screen, LINE_COLOR, (50, 400), (550, 400), LINE_WIDTH)


running = True
while running:
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            running = False
    
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // (WIDTH // GRID_SIZE)
            row = y // (HEIGHT // GRID_SIZE)
            
    
    
    
    draw_board()
        
    pg.display.update()
    