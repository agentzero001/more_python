import pygame as pg
import sys

vec2 = pg.math.Vector2

class Tictactoe:
    
    def __init__(self, game, W_SIZE, screen):
        self.LINE_COLOR = (80, 80, 80)
        self.W_SIZE = W_SIZE
        self.screen = screen
        self.board = [['' for i in range(3)] for j in range(3)]
        self.GREY = (80, 80, 80)
        self.OBJ_SIZE = 60
        self.OBJ_WIDTH = 15
        self.GRID_SIZE = 3
        self.CELL_SIZE = self.W_SIZE // 3
        self.player_turn = 'X'
        self.game_over = False
    
    def check_win(self, player):
        for i in range(self.GRID_SIZE):
            if all(self.board[i][j] == player for j in range(self.GRID_SIZE)):
                return (True, 'h', i) 

        for col in range(self.GRID_SIZE):
            if all(self.board[row][col] == player for row in range(self.GRID_SIZE)):
                return (True, 'v', col) 

        if all(self.board[i][i] == player for i in range(self.GRID_SIZE)):             
            return (True, 'd1', None)
            
        if all(self.board[i][3 - i - 1] == player for i in range(self.GRID_SIZE)):
            return (True, 'd2', None)
                 
        return (False, None, None)    
        
    def draw_XO(self):
        
        current_cell = vec2(pg.mouse.get_pos()) // self.CELL_SIZE
        if self.board[int(current_cell[1])][int(current_cell[0])] == '':
            self.board[int(current_cell[1])][int(current_cell[0])] = self.player_turn            
            
        if self.check_win(self.player_turn)[0]:
            line_orientation = self.check_win(self.player_turn)[1]
            a = self.check_win(self.player_turn)[2]
            self.game_over = True
            
        if self.game_over:
            self.screen.fill((110,110,110))
            if line_orientation == 'h':
               pg.draw.line(self.screen,
                            (0, 0, 0), 
                            (0, 100 + self.W_SIZE // 3 * a ),
                            (self.W_SIZE, 100 + self.W_SIZE // 3 * a),
                            20)
            if line_orientation == 'v':
                pg.draw.line(self.screen,
                            (0, 0, 0), 
                            (100 + self.W_SIZE // 3 * a, 0 ),
                            (100 + self.W_SIZE // 3 * a, self.W_SIZE),
                            20)
                
            if line_orientation == 'd1':
                pg.draw.line(self.screen,
                            (0, 0, 0), 
                            (0, 0),
                            (self.W_SIZE, self.W_SIZE),
                            20)
                
            if line_orientation == 'd2':
                pg.draw.line(self.screen,
                            (0, 0, 0), 
                            (self.W_SIZE, 0),
                            (0, self.W_SIZE),
                            20)
                                         
            print('Player {} win'.format(self.player_turn))          
            
        self.player_turn = 'O' if self.player_turn == 'X' else 'X'
        print(self.board)                
    
    def run(self):
        for x in range(1,3):
            pg.draw.line(self.screen, self.LINE_COLOR, (50, x*200), (self.W_SIZE - 50, x*200), 5)
            pg.draw.line(self.screen, self.LINE_COLOR, (x*200, 50), (x*200, self.W_SIZE - 50), 5)
               
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                if self.board[row][col] == 'X':
                    x = col * self.W_SIZE // self.GRID_SIZE + self.W_SIZE // (2 * self.GRID_SIZE)
                    y = row * self.W_SIZE // self.GRID_SIZE + self.W_SIZE // (2 * self.GRID_SIZE)
                    pg.draw.line(self.screen,
                                 self.GREY, 
                                 (x - self.OBJ_SIZE, y - self.OBJ_SIZE), 
                                 (x + self.OBJ_SIZE, y + self.OBJ_SIZE), 
                                 self.OBJ_WIDTH)
                    pg.draw.line(self.screen, 
                                 self.GREY, 
                                 (x - self.OBJ_SIZE, y + self.OBJ_SIZE), 
                                 (x + self.OBJ_SIZE, y - self.OBJ_SIZE), 
                                 self.OBJ_WIDTH)
                elif self.board[row][col] == 'O':
                    x = col * self.W_SIZE // self.GRID_SIZE + self.W_SIZE // (2 * self.GRID_SIZE)
                    y = row * self.W_SIZE // self.GRID_SIZE + self.W_SIZE // (2 * self.GRID_SIZE)
                    pg.draw.circle(self.screen, self.GREY, (x, y), self.OBJ_SIZE, self.OBJ_WIDTH)
   
            
class Game:
    def __init__(self, W_SIZE=600):
        pg.init()
        self.screen = pg.display.set_mode([W_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.tic_tac_toe = Tictactoe(self, W_SIZE, self.screen)
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.tic_tac_toe.draw_XO()
    
    def run(self):
        self.screen.fill((20, 20, 20))
        while True:            
            self.tic_tac_toe.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
    
    