# board -> input values and display them on the table
# 2 players -> change player
# check winner / tie
# check gameover

def printBoard(board):
    for row in board:
        print("|".join(row))
        print("-----")

def addValues(board, row, column, player):
    if board[row][column] == " ":
        board[row][column] = player
        return True
    return False
    # pass

def checkWinner(board, player):
    # for i in range(3):
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
        
    # pass

def checkTie(board):
    for row in board:
        if " " in row:
            return False
    return True
    # pass

def playTicTacToe():
    board = [[" "] * 3 for _ in range(3)]
    
    # for row in board:
    #     print("|".join(row))
    #     print("-----")
        
    player = "X"
    
    while True:
        # print(board)
        printBoard(board)
        print("Player: ", player)
        
        try:
            row = int(input("Enter any number between 0 and 2: "))
            column = int(input("Enter any number between 0 and 2: "))
            
        except ValueError:
            print("Enter a number!")
            continue

        if row in range(3) and column in range(3):
            if addValues(board, row, column, player):
                if checkWinner(board, player):
                    # print(board)
                    printBoard(board)
                    print(f"{player} Won!")
                    break
                
                if checkTie(board):
                    print("A Tie!")
                    break
                
                player = "0" if player == "X" else "X"
            else:
                print("Slot already takem, Try again!")
                continue
            # checkTie(board)
            
        else:
            print("Enter One number!")
            continue
        

playTicTacToe()