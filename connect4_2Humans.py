import numpy as np
import pygame
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
ROW_COUNT = 6
COLUMN_COUNT = 7
game_over = False
turn = 1
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)

pygame.init()
board = np.zeros((ROW_COUNT,COLUMN_COUNT))
myfont = pygame.font.SysFont("monospace", 75)
screen = pygame.display.set_mode(size)

def drop_piece(row, col, piece):
	board[row][col] = piece

def is_valid_location(col):
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def print_board():
	print(np.flip(board, 0))

def winning_move(piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def draw_board():
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

while not game_over:
	draw_board() 
	for event in pygame.event.get():
		pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.MOUSEMOTION:
			posx = event.pos[0]
			color = YELLOW
			if turn == 1: color = RED
			pygame.draw.circle(screen, color, (posx, int(SQUARESIZE/2)), RADIUS)
		if event.type == pygame.MOUSEBUTTONDOWN:
			posx = event.pos[0]
			col = posx // SQUARESIZE
			if is_valid_location(col):
				row = get_next_open_row(col)
				drop_piece(row, col, turn)
			if winning_move(turn):
				label = myfont.render(f"Player {turn} wins!!", turn, RED)
				screen.blit(label, (40,10))
				game_over = True
			draw_board() 
			print_board()
			turn = 3 - turn
			if game_over:
				pygame.time.wait(3000)
		pygame.display.update()
