# ticTacToe 

# two players [x, 0]
# board - 3*3
# row and columns [0, 1, 2]
# which player
# input - pla

# check if the input is valid
# add value to board
# change player
# check if there is a winner
# check if there is a tie
# check if the game is over

def printBoard(board):
    for row in board:
        print("|".join(row))
        print("-----")
    # print("\n")
    
def addValue(board, row, column, person):
    if board[row][column] == " ":
        board[row][column] = person
        return True
    return False

def checkWinner(board, person):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == person: # 00, 01, 02 or 10, 11, 12 or 20, 21, 22
            return True
        if board[0][i] == board[1][i] == board[2][i] == person: # 00, 10, 20 or 01, 11, 21 or 02, 12, 22
            return True
    if board[0][0] == board[1][1] == board[2][2] == person: # 00, 11, 22
        return True
    if board[0][2] == board[1][1] == board[2][0] == person: # 02, 11, 20
        return True
    return False

def checkTie(board):
    for row in board:
        if " " in row:
            return False
    return True

def gameOver(board, person):
    return checkWinner(board, person) or checkTie(board)


def playGame():
    # for i in range(3) *2
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ] 
    # print(board) #board[1][0]
    person = "X"
    
    while True:
        printBoard(board)
        print("player " + person)
    
        try:
            row = int(input("Enter a row (0, 1, or 2): "))
            column = int(input("Enter a column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter integers 0, 1, or 2.")
            continue
        
        if row in range(3) and column in range(3):
            if addValue(board, row, column, person):
                if checkWinner(board, person):
                    printBoard(board)
                    print(person + " wins!")
                    break # game over
                if checkTie(board):
                    printBoard(board)
                    print("It's a tie!")
                    break # game over
                person = "0" if person == "X" else "X"
            else:
                print("This position is already taken. Try again.")
        else:
            print("Invalid input. Please enter 0, 1, or 2.")
    
    return "Game Over"
 
    
# print(playGame())
playGame()
