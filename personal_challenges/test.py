# # hangman

# # list of words
# # new_word - _
# # lives 6 
# # 

# import random

# words = ['google', 'person', 'openai']

# def playGame():
#     # comp_choice = random.choice(words)
#     comp_choice = "google"
#     new_word = ["_"] * len(comp_choice)
#     wrong_guesses = []
#     lives = 6
    
#     while "_" in new_word and lives >0:
#         print("word:" + "".join(new_word))
#         print(f"Wrong guesses {', '.join(wrong_guesses)}")
#         print(f"Lives {lives}")
        
#         guess = input("Guess a letter ").lower()
        
#         if not guess.isalpha and len(guess) != 1:
#             print("Input one letter!")
#             continue
        
#         if guess in comp_choice:
#             for i, letter in enumerate(comp_choice):
#                 if letter == guess:
#                     if new_word[i] != "_":
#                         continue
#                     new_word[i] = guess
#                     print("Good guess")
#                     break
#         else:
#             lives -= 1
#             wrong_guesses.append(guess)
#             print("Wrong guess!")


#         if "_" not in new_word:
#             print("Congratulations You won! word is ", comp_choice)
    
#     if lives == 0:
#         print('You ran out of lives! word was ', comp_choice)
        
            
# playGame()
            
    
    
    
# tictactoe

# board lists
# player 2 "x"/"0"
# functions: printBoard, addValues, CheckWinner, CheckTie, game()

def printBoard(board):
    for row in board:
        print(row)
        # print("|")
        # print("-----")
        
def addValues(board, player, row, column):
    if board[row][column] == " ":
        board[row][column] = player
        return True
    return False
    # pass

def checkWinner(board, player):
    for i in range(3):
        # 0,0, 0,1, 0,2
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # column 
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # 0,0 1,1 2,2
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    # 0,2 1,1 2,0
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    # pass

def playGame():
    board = [[" "] *3 for _ in range(3)]
    player = "X"
    
    while True:
        print("Player", player)
        print(" \n")
        printBoard(board)
        
        try:
            row = int(input("Input a number in range 1-2: "))
            column = int(input("Input a number in range 1-2: "))
        except ValueError:
            print("Input one number!")
            continue
        
        if addValues(board, player, row, column):
            if checkWinner(board, player):
                printBoard(board)
                print(player + " wins!")
                break
            # checkWinner / tie
            player = "0" if player == "X" else "X"
        else:
            print("Space is not available")
        
        
playGame()
    
    
