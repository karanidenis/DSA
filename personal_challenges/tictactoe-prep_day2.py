# board 
# 2 players -> change players
# add player value to the board and print it
# check winner or tie

def printBoard(board):
    for row in board:
        print("|".join(row))
        print("-----")

def addValues(board, row, column, person):
    if board[row][column] == " ":
        board[row][column] = person
        return True
    return False
    # pass

def checkWinner(board, person):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == person:
            return True
        if board[0][i] == board[1][i] == board[2][i] == person:
            return True
    if board[0][0] == board[1][1] == board[2][2] == person:
        return True
    if board[0][2] == board[1][1] == board[2][0] == person:
        return True
    # pass

def checkTie(board):
    for row in board:
        if " " not in row:
            return False
    return False
    # pass

def playGame():
    board = [[" "]*3 for _ in range(3)]    
    player = "0"
    
    while True:
        print("\n")
        printBoard(board)
        print(f"Player: {player}")
        
        try:
            row = int(input("enter a number between 0 and 2: "))
            column = int(input("enter a number between  0 and 2: "))
        except ValueError:
            print("Enter a number!")
            continue
        
        if row in range(3) and column in range(3):
             # add values - if true- values added else false
            if addValues(board, row, column, player):
                #  check if values added are a win or tie
                if checkWinner(board, player):
                    printBoard(board)
                    print("You won!")
                    break
                
                if checkTie(board):
                    print("Tie!")
                    break
                player = "X" if player == "0" else "0"
            else:
                print("Space already filled!")
                continue
            
        else:
            print("Enter a value between 0 and 2!")
            continue
        
        
        
playGame()