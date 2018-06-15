from random import randint

print ("""
Welcome to Tic Tac Toe!
You must get a horizontal, vertical, or diagonal line of 3 to win.
""")
board = []
for i in range(3):
    board.append(["•"] * 3)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)