import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT, COLUMN_COUNT))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT - 1][col] == 0 #only need to check top row to see if valid location

def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board, 0)) #makes player inputs bottom to top rather than top to bottom

def winning_move(board, piece):
	#Check horizontal locations for win
	for c in range(COLUMN_COUNT - 3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	#Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT - 3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	#Check positive diagonal slope locations for win
	for c in range(COLUMN_COUNT - 3):
		for r in range(ROW_COUNT - 3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	#Check negative diagonal slope locations for win
	for c in range(COLUMN_COUNT - 3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

#initialise board
board = create_board()
print_board(board)
#initialise game_over as False
game_over = False
turn = 0

while not game_over:
	#Ask for player 1 input
	if turn == 0:
		col = int(input("Player 1 Make your selection(0-6): "))
		#Player 1 will drop a piece on the board
		if is_valid_location(board, col):
			row = get_next_open_row(board, col)
			drop_piece(board, row, col, 1)

		if winning_move(board, 1):
			game_over = True
			print("Player 1 wins!")

	#Ask for player 2 input
	else:
		col = int(input("Player 2 Make your selection(0-6): "))
		#Player 2 will drop a piece on the board
		if is_valid_location(board, col):
			row = get_next_open_row(board, col)
			drop_piece(board, row, col, 2)

		if winning_move(board, 2):
			game_over = True
			print("Player 2 wins!")

	print_board(board)

	turn += 1
	turn = turn % 2
