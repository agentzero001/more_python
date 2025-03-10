from settings import * 
from random import choice


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        super().__init__(tetromino.tetris.sprite_group)
        self.tetromino = tetromino
        self.pos       = vec(pos) + INIT_POS_OFFSET
        self.next_pos  = vec(pos) + NEXT_POS_OFFSET
        self.alive     = True
        self.image     = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.color     = TETROMINOES[tetromino.shape][1]        
        pg.draw.rect(self.image,
                     self.color,
                     (1, 1, TILE_SIZE - 2, TILE_SIZE - 2),
                     border_radius=8)       
        self.rect = self.image.get_rect()      
        
    def is_alive(self):
        if not self.alive:
            self.kill()
        
    def rotate(self, pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos
        
    def set_rect_pos(self):
        pos = [self.next_pos, self.pos][self.tetromino.current]
        self.rect.topleft = pos * TILE_SIZE
        
    def update(self):
        self.is_alive()
        self.set_rect_pos()
    
    def collision(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (
           y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True     

class Tetromino:
    def __init__(self, tetris, current=True):
        self.tetris = tetris
        self.shape = choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape][0]]
        self.landed = False
        self.current = current
        
    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]
        
        if not self.is_collide(new_block_positions):
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]
        
    def is_collide(self, block_position):
        return any(map(Block.collision, self.blocks, block_position))
    
    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        new_block_positions = [block.pos + move_direction for block in self.blocks]
        if not self.is_collide(new_block_positions):
            for block in self.blocks:
                block.pos += move_direction
        elif direction == 'down':
            pg.time.wait(500)
            self.landed = True
            #self.tetris.sprite_group.empty()            
    
    def update(self):
        self.move(direction='down')