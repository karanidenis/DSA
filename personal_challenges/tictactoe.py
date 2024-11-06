# TictacToe game

# board
# players
# add values to board
# check for winner/tie
# 

# functions:
# print the board
# add value - uses rows and columns. - check if space elese asks player to play again
# check winner - logic to check winner - if true, break else checck tie
# check tie - if no space, it's a tie. 


def printboard(board):
    for row in board:
    #     print("|".join(row))
        print("-----")
    # print(board)

def addValues(board, person, row, column):
    if " " in board[row][column]:
        board[row][column] = person
        return True
    return False

def checkWinner(board, player):
    for i in range(3):
        
    # pass

def checkTie(board):
    pass


def playGame():
    board = [[" "] *3 for _ in range(3)]
    # print(board)
    person = "X"
    
    while True:
        printboard(board)
        print("person", person)
        
        try:
            row = int(input("Enter a row-value in range 0-2: "))
            column = int(input("Enter a column-value in range 0-2: "))
        except ValueError:
            print("Invalid number! Try again")
            continue
        
        if row in range(3) and column in range(3):
            # add value
            if addValues(board,row, column, person):
                
            # check winner
            # check tie

playGame()