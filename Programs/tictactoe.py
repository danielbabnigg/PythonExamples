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

turnsleft = 5
isdone = 0
print ("Turns left:", turnsleft)
print_board(board)

while turnsleft > 0:
    if isdone == 1:
        break
    guessrow = int(input("What row? "))
    guesscol = int(input("What column? "))
    if guessrow not in range(4) or guesscol not in range(4):
        print ("Invalid entry!")
        print ("")
        print ("Turns left:", (turnsleft))
    elif board[guessrow-1][guesscol-1] == "X":
        print ("You entered that one already!")
        print ("")
        print ("Turns left:", (turnsleft))
    elif board[guessrow-1][guesscol-1] == "O":
        print ("Your opponent entered that one already!")
        print ("")
        print ("Turns left:", (turnsleft))
    else:
        board[guessrow-1][guesscol-1] = "X"
        randrow = randint(0,2)
        randcol = randint(0,2)
        while turnsleft > 1:
            if board[randrow][randcol] == "O":
                randrow = randint(0,2)
                randcol = randint(0,2)
            elif board[randrow][randcol] == "X":
                randrow = randint(0,2)
                randcol = randint(0,2)
            elif board[randrow][randcol] == board[guessrow-1][guesscol-1]:
                randrow = randint(0,2)
                randcol = randint(0,2)
            else:
                board[randrow][randcol] = "O"
                if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X"):
                    print ("")
                    isdone = 1
                    print ("Congratulations, you win!")
                    isdone = 1
                    break
                elif (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X"):
                    print ("")
                    isdone = 1
                    print ("Congratulations, you win!")
                    break
                elif (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"):
                    print ("")
                    isdone = 1
                    print ("Congratulations, you win!")
                    break
                elif (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X"):
                    print ("")
                    isdone = 1
                    print ("Congratulations, you win!")
                    break
                elif (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"):
                    print ("")
                    isdone = 1
                    print ("Congratulations, you win!")
                    break
                elif (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
                    print ("")
                    isdone = 1
                    print ("Congratulations, you win!")
                    break
                elif (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"):
                    print ("")
                    isdone = 1
                    print ("Congratulations, you win!")
                    break
                elif (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
                    print ("")
                    isdone = 1
                    print ("Congratulations, you win!")
                    break
                elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O"):
                    print ("")
                    isdone = 1
                    print ("Sorry, you lose!")
                    break
                elif (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O"):
                    print ("")
                    isdone = 1
                    print ("Sorry, you lose!")
                    break
                elif (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
                    print ("")
                    isdone = 1
                    print ("Sorry, you lose!")
                    break
                elif (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O"):
                    print ("")
                    isdone = 1
                    print ("Sorry, you lose!")
                    break
                elif (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O"):
                    print ("")
                    isdone = 1
                    print ("Sorry, you lose!")
                    break
                elif (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
                    print ("")
                    isdone = 1
                    print ("Sorry, you lose!")
                    break
                elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"):
                    print ("")
                    isdone = 1
                    print ("Sorry, you lose!")
                    break
                elif (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
                    print ("")
                    isdone = 1
                    print ("Sorry, you lose!")
                    break
                break
        if isdone == 0:
            print ("")
            print ("Turns left:", (turnsleft - 1))
            turnsleft = turnsleft - 1
    if isdone == 0:
        print_board(board)
    elif isdone == 1:
        board[randrow][randcol] = "•"
        print_board(board)
else:
    print ("Game Over, you lost!")