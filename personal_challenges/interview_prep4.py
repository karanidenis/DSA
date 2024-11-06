# hangam

# words > random specifc word ✔
# new word of underscores  > list > add letters/guess ✔
# list > wrong guesses > ✔ 
# lives > track gameover ✔
# check for gameover > no underscores / lives = 0

import random

words = ['google', 'pareto', 'openai']

def playHangam():
    rand_word = random.choice(words)
    print(rand_word)
    new_word = ["_"] * len(rand_word)
    # print("your_word: ",", ".join(new_word))

    wrong_gusses = []
    lives = 6

    while lives > 0 and "_" in new_word:
        print("\nyour_word: ",", ".join(new_word))
        print("Lives remaining: ", lives)
        print("Wrong guesses: ", ', '.join(wrong_gusses))

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha or len(guess) != 1:
            print("Enter only one letter!")
            continue
        
        if guess in wrong_gusses or guess in new_word:
            print("Already guessed this letter!")
            continue
        
        if guess in rand_word:
            for i, letter in enumerate(rand_word):
                if letter == guess:
                    new_word[i] = guess
                    # print(i)
                    print("Good guess!")
        else:
            lives -= 1
            wrong_gusses.append(guess)
            print("Wrong guess!")
    
        if "_" not in new_word:
            print(f"You won! the word is {rand_word}")
            
        if lives == 0:
         print(f"You are out of lives! The word was {rand_word}")

        # break

playHangam()


# 3 by 3 board > print it > show how players add values/tick boxes > list of lists ✔
# 2 players > change them
# use row and columns > add values to box 
# check winner 

def printBoard(board):
    for row in board:
        print("|".join(row))
        print("-------")
        
def addValues(board, row, column, player):
    if board[row][column] == " ":
        board[row][column] = player
        return True
    return False

def checkWinner(board, player):
    # 00, 11, 22, 33
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == player:
        return True
    # 03, 12, 21, 30
    if board[0][3] == board[1][2] == board[2][1] == board[3][0] == player:
        return True
    for i in range(4):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == player:
            return True
        if board[0][i] ==  board[1][i] == board[2][i] == board[3][i] == player:
            return True
    
    # pass


def playTicTacToe():
    board = [[" "] * 4 for _ in range(4)]
    
    # print(board)
    # for row in board:
    #     print("|".join(row))
    #     print("-------")
    
    player = "X"
    
    while True:
        printBoard(board)
        print("\nPlayer", player)
        
    
        try:
            row = int(input("Enter a value bwtween 0 and 3: "))
            column = int(input("Enter a value bwtween 0 and 3: "))
        except ValueError:
            print("Enter one number!")
            continue
        
        if row in range(4) and column in range(4):
            if addValues(board, row, column, player):
                if checkWinner(board, player):
                    printBoard(board)
                    print(f"{player} Won!")
                    break
                
            else:
                print("Slot on the board is already taken!")
            
            # checkwinner(board, player)
            player = "0" if player == "X" else "X"
        else:
            print("Enter a number between 0 and 2!")
        
        # break
    
# playTicTacToe()