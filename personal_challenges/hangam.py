# # Create a Hangman game with the following requirements:
# Choose a random word from a predefined list.
# Display the word as underscores, revealing correct guesses.
# Allow the player to input letter guesses.
# Track and display incorrect guesses.
# Implement a lives system (e.g., 6 lives).
# End the game when the word is guessed or lives run out.
# Display a win/lose message and reveal the word.

# word of _
# random chosen word, & list of words
# display word
# reduce lives
# save guess for check if repeated
# check for gameover - if  no more _ in word or lives < 1

import random

def addWord(comp_choice, new_word, guess):
    correct = False
    # if guess in comp_choice:
    for i, letter in enumerate(comp_choice):
        if letter == guess:
            new_word[i] = guess
            correct = True
    return new_word, correct


words = ['google', 'openai', 'person']


def playGame():
    comp_choice = random.choice(words)
    new_word = ["_"] * len(comp_choice)
    lives = 6
    wrong_guesses = []
    
    while True:
        # print(new_word)
        print("\nWord: " + " ".join(new_word))
        print("Lives left ", lives)
        print("incorrect guesses, ", ','.join(wrong_guesses))
        
        guess = input("enter a letter: ")
        
        if not guess.isalpha() and len(guess) != 1:
            print("Incorrect Input! Input one letter")
            continue
        
        if guess in new_word or guess in wrong_guesses:
            print("You ahave already guessed that letter!")
            continue
        
        new_word, correct = addWord(new_word, comp_choice, guess)
        
        if correct:
            print("Good guess")
            # print()
        else:
            lives -= 1
            wrong_guesses.append(guess)
            print("Incorrect Guess!")
        print(new_word)
            
        if "_" not in new_word:
            print("Congratulations! you have won! The word was ", comp_choice)
            return
    if lives == 0:
        print("Game over! You ran out of lives! The word was " , comp_choice)
        
        
playGame()