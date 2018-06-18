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

randrow = randint(0, len(board) - 1)
randcol = randint(0, len(board) - 1)

turnsleft = 5
print ("Turns left:", turnsleft)
print_board(board)

while turnsleft > 0:
    guessrow = int(input("What row? "))
    guesscol = int(input("What column? "))
    if guessrow not in range(4) or guesscol not in range(4):
        print ("Invalid entry!")
        print ("")
    elif board[guessrow-1][guesscol-1] == "X":
        print ("You entered that one already.")
        print ("")
    elif board[guessrow-1][guesscol-1] == "O":
        print ("Your opponent entered that one already.")
        print ("")
    else:
        board[guessrow-1][guesscol-1] = "X"
        comguess = board[randint(0,2)][randint(0,2)]
        if comguess == "O":
            comguess = board[randint(0,2)][randint(0,2)]
            comguess = "O"
        elif comguess == "X":
            comguess = board[randint(0,2)][randint(0,2)]
            comguess = "O"
        elif comguess == board[guessrow-1][guesscol-1]:
            comguess = board[randint(0,2)][randint(0,2)]
            comguess = "O"
        else:
            comguess = "O"
        print ("")
        print ("Turns left:", (turnsleft - 1))
        turnsleft = turnsleft - 1
    print_board(board)
else:

    print ("Game Over, you lost!")