TILE_SIZE = 64
TILE_SIZE_05 = TILE_SIZE // 2
SOME_MORE_SPACE = TILE_SIZE * 6

WIN_SIZE = [TILE_SIZE * 8 + SOME_MORE_SPACE] * 2

WIDTH, HEIGHT = [TILE_SIZE * 8] * 2

FPS = 60

BACKGROUND_COLOR = (0, 0, 0)
BOARD_COLOR_1 = (30, 0, 0)
BOARD_COLOR_2 = (60, 0, 0)
LETTER_COLOR = (100, 0, 0)

SYMBOLS = [list(range(8, 0, -1)), 'ABCDEFGH']

X_POS_NUMBERS = [SOME_MORE_SPACE // 2 - TILE_SIZE_05, SOME_MORE_SPACE // 2 + WIDTH + TILE_SIZE_05]
Y_POS_LETTERS = [SOME_MORE_SPACE // 2 - TILE_SIZE_05, SOME_MORE_SPACE // 2 + HEIGHT + TILE_SIZE_05]
XY_POS = [X_POS_NUMBERS, Y_POS_LETTERS]

