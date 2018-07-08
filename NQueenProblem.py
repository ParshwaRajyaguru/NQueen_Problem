# N-Queen Problem Sloved by using AI's Constrain Satisfaction Problem(CSP) Algorithm - Backtracking Search 
# Print of all possible N-Queens' position on the board as result

global N
# Explicitly give number of Queens in the N-Queen problem
N = 8


# Function for validate whether Queen's position is correct or not
def validPosition(board, row, column):
	# Loop each column for given number of rows
	# Check for column
	for r in range(row):
		if board[r][column] == 1:
			return False


	# Check for positive Diagonal
	r = row
	col = column
	while ((r >= 0) & (col < N)):
		if board[r][col] == 1:
			return False
		r = r - 1
		col = col + 1


	# Check for negative Diagonal
	i = row
	j = column
	while ((i >= 0) & (j >= 0)):
		if board[i][j] == 1:
			return False
		j = j - 1
		i = i - 1


	return True



# Print Board of N-Queen Problem
def printResult(board):
	print ("N-Queen Problem Board:")
	for i in range(N):
		for j in range(N):
			if (board[i][j] == 1):
				print ('Q', end = '  ')
			else:
				print ('-', end = '  ')
		print ()
	print ()
	print ()

	return



# Function to find Queens' correct position and arrange it 
def arrangeNQueue (board, row, column):
	# if row is reach to end of array's max row, it print one of the posiible arrangement of N-Queen Problem
	if ((row == N) & (column == 0)):
		printResult(board)
		return

	
	for c in range(N):
		if (validPosition(board, row, c)):
			board[row][c] = 1

			arrangeNQueue(board, row+1, 0)
	
			board[row][c] = 0



# Enter N Queen as user input
# N = int(input("Enter Queue: "))

board = [[0 for x in range(N)] for y in range(N)]

arrangeNQueue (board, 0, 0)
