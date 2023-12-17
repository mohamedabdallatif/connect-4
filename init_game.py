import numpy as np

# Game Colors
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (219, 37, 37)
TEAL = (8, 152, 139)
BRIGHT_TEAL = (62, 227, 212)
GREEN = (0, 200, 0)
BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0, 255, 0)
SCREEN_BACKGROUND = (160, 184, 188)

# Game Screen Vairables
EMPTY = 0
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
WINDOW_LENGTH = 4
RADIUS = int(SQUARESIZE/2 - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height + 20)

# Game Logic Variables
input_depth = '1'
with_alpha_beta = False
