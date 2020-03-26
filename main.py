print()
print("Start program:  Battleship")
print()

board = []

for row in range(5):
	board.append(["_"] * 5)
for row in board: 
	print(" ".join(row))

