"""
Memory game: on a grid of 5x5, pairs of letters area assigned at random. At the beginning all letters are
'covered'. The user must pick two positions that will be revealed. If the revealed match they stay revealed.
The player wins if all letters are revealed.

Design the models and entities required to play the memory game.
You can assume there is a pre-defined user_input function which returns the current user's input.
"""

import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
print(len(letters))
# double the letters
letters = letters * 2
# print(len(letters))
# print(letters)

# shuffle the letters
random.shuffle(letters)
# print(letters)

board = [["X"] * 5 for _ in range(5)]
# print(board)

board_2 = [letters[i:i+5] for i in range(0, 25, 5)]
# print(board_2)
print(letters[i:i+5] for i in range(0, 25, 5))

def print_board(board):
    for row in board:
        print("|".join(row))
        print("---------")
        
print_board(board)
print()
print_board(board_2)
