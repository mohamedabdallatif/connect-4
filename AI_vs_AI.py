import math
import random
from init_game import *

AI_Min = 0
AI_Max = 1
AI_Min_PIECE = 1
AI_Max_PIECE = 2

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT - 1][col] == 0

def get_valid_locations(board):
	return [
     	col for col in range(COLUMN_COUNT) 
        if is_valid_location(board, col)
    ]

def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def winning_move(board, piece):
    # Check horizontal locations for win
	for c in range(COLUMN_COUNT - 3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True
	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT - 3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT - 3):
		for r in range(ROW_COUNT - 3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT - 3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def eval_fun(window, piece):
	score = 0
	opp_piece = AI_Min_PIECE
	if piece == AI_Min_PIECE:
		opp_piece = AI_Max_PIECE
	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
		score += 2
	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
		score -= 4
	return score

def score_position(board, piece):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(ROW_COUNT):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(COLUMN_COUNT - 3):
			window = row_array[c : c + WINDOW_LENGTH]
			score += eval_fun(window, piece)

	## Score Vertical
	for c in range(COLUMN_COUNT):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(ROW_COUNT - 3):
			window = col_array[r : r + WINDOW_LENGTH]
			score += eval_fun(window, piece)

	## Score posiive sloped diagonal
	for r in range(ROW_COUNT - 3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
			score += eval_fun(window, piece)

	for r in range(ROW_COUNT - 3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r - i + 3][c + i] for i in range(WINDOW_LENGTH)]
			score += eval_fun(window, piece)

	return score

def terminal_test(board):
	return winning_move(board, AI_Min_PIECE) or winning_move(board, AI_Max_PIECE) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, cur_AI):
	valid_locations = get_valid_locations(board)
	is_terminal = terminal_test(board)
	if depth == 0 or is_terminal:
		if is_terminal:
			if winning_move(board, AI_Max_PIECE):
				return (None, 1e18)
			elif winning_move(board, AI_Min_PIECE):
				return (None, -1e18)
			else:
				return (None, 0)
		else:
			return (None, score_position(board, AI_Max_PIECE))
	if cur_AI == AI_Max:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, AI_Max_PIECE)
			new_score = minimax(b_copy, depth - 1, alpha, beta, AI_Min)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
	else:
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, AI_Min_PIECE)
			new_score = minimax(b_copy, depth - 1, alpha, beta, AI_Max)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
	return column, value

def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == AI_Min_PIECE:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == AI_Max_PIECE: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

def play_AI_vs_AI(depth):
    draw_board(board)
    turn = random.randint(AI_Min, AI_Max)
    while not game_over:
        if turn == AI_Max:
            col, _ = minimax(board, depth, -math.inf, math.inf, AI_Max)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_Max_PIECE)
                if winning_move(board, AI_Max_PIECE):
                    label = myfont.render("Max wins!!", 1, RED)
                    print('MAX wins!!')
                    screen.blit(label, (40,10))
                    game_over = True
        elif turn == AI_Min and not game_over:			
            col, _ = minimax(board, depth, -math.inf, math.inf, AI_Min)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_Min_PIECE)
                if winning_move(board, AI_Min_PIECE):
                    label = myfont.render("MIN wins!!", 1, YELLOW)
                    print('MIN wins!!')
                    screen.blit(label, (40,10))
                    game_over = True
        draw_board(board)
        pygame.time.wait(500)
        turn = (turn + 1) % 2

    if game_over:
        pygame.time.wait(3000)
