from random import randint # import the random module

def random_row(board): # sets random row
	return randint(0,len(board) -1)

def random_col(board): # sets random col
	return randint(0,len(board) -1)

def print_board(board): # prints board before every turn
	for row in board: # for loop that modifies elements to join and removes ,
		print(" ".join(row)) # board constructed
 
# client code
print()
print("Start Game:  Battleship")
print()

board = [] # start board construction w/ empty list

for row in range(5): # creates a list range from 0-4
	board.append(["O"] * 5) # inputs "string" across range at each element 


ship_row = random_row(board) # saves random row
ship_col = random_col(board) # saves random col


while True: # infinite loop
	print_board(board)
	guess_row = int(input("Set guess row: ")) # terminal input of value for row
	guess_col = int(input("Set guess col: ")) # terminal input of value for col
	
	# make sure it's valid
	if guess_row not in range(5) or guess_col not in range(5):
		print("Oops, that's not even in the ocean.")

	# gets a hit
	elif guess_row == ship_row and guess_col == ship_col:
		print("""
		Congratulations! You sank my battleship!""")
		break
	elif board[guess_row][guess_col] == "X":
		print("You guessed that already")
	
	# gets a miss
	else:
		print("You missed my battleship!")
		board[guess_row][guess_col] = "X"

		