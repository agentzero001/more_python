from settings import * 
from random import choice


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET
        
        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill((60,60,60))        
        self.rect = self.image.get_rect()
        
    def set_rect_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE
        
    def update(self):
        self.set_rect_pos()
    
    def collision(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (
           y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True     

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        self.landed = False
        
    def is_collide(self, block_position):
        return any(map(Block.collision, self.blocks, block_position))
    
    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        new_block_positions = [block.pos + move_direction for block in self.blocks]
        is_collide = self.is_collide(new_block_positions)
        if not is_collide:
            for block in self.blocks:
                block.pos += move_direction
        elif direction == 'down':
            self.landed = True
            #self.tetris.sprite_group.empty()            
    
    def update(self):
        self.move(direction='down')