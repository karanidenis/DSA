# # Create a Hangman game with the following requirements:
# Choose a random word from a predefined list.
# Display the word as underscores, revealing correct guesses.
# Allow the player to input letter guesses.
# Track and display incorrect guesses.
# Implement a lives system (e.g., 6 lives).
# End the game when the word is guessed or lives run out.
# Display a win/lose message and reveal the word.

# list of words
# display underscores
# allow player to input letters
# check guess
# have lives e.g = 6
# check gameover - no underscores or lives == 0
# display won/lost message

import random

words = ['doctor', 'openai', 'person', 'spaces']


def hangamGame():
    # comp_word = random.choice(words)
    comp_word = 'google'
    # print(comp_word)
    underscores_wrd = ["_"] * len(comp_word)
    # print(underscores_wrd)
    incorrect_guesses = []
    
    lives = 6
    
    while lives > 0 and "_" in underscores_wrd:
        print("\nWord is", ", ".join(underscores_wrd))
        print(f"Lives count: {lives}")
        
        guess = input("Input a letter: ")
        
        if len(guess) != 1 or not guess.isalpha:
            print("Input only one letter!")
            continue
        
        if guess in underscores_wrd or guess in incorrect_guesses:
            print("Already used this letter, try a different letter!")
            continue
        
        if guess in comp_word:
            for i, letter in enumerate(comp_word):
                if letter == guess:
                    if underscores_wrd[i] != "_":
                        continue
                    underscores_wrd[i] = guess
                    print("Good guess!")
                    break
        else:
            lives -= 1
            incorrect_guesses.append(guess)
            print("Incorrect guess, try again!")
            
        if "_" not in underscores_wrd:
            print(f"You won! The word is {comp_word}")
            return
    if lives == 0:
        print("You lost. You are out of lives!")
        
    return 


hangamGame()
# if __name__ == '__main__':
    # hangamGame()
        
        