import pygame
import numpy as np

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
EMPTY = 0
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
game_over = False
WINDOW_LENGTH = 4

pygame.init()
board = np.zeros((ROW_COUNT,COLUMN_COUNT))
myfont = pygame.font.SysFont("monospace", 75)
screen = pygame.display.set_mode(size)
