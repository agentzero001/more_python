WIN_SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 60
TILE_SIZE = 64

COLORS = ((255, 0, 0), (0, 0, 255), (255, 255, 0))
NUMBERS = tuple(range(1,9))
POS = [(j*100 + 100, i*100 + 100) for i in range(3) for j in range(8)]


CARD_DATA = [(COLORS[i // 8], POS[i], NUMBERS[i % 8]) for i in range(24)]

print(CARD_DATA)