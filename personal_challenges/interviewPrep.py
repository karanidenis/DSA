# Create a Hangman game with the following requirements:
# Choose a random word from a predefined list.
# Display the word as underscores, revealing correct guesses.
# Allow the player to input letter guesses.
# Track and display incorrect guesses.
# Implement a lives system (e.g., 6 lives).
# End the game when the word is guessed or lives run out.
# Display a win/lose message and reveal the word.


# words list 
# choose a random word - random
# display words as _ > rnd_wrd
# allow user to input letter
# check if letter in word
# add letter to rnd_wrd + add lives count
# if word guessed is correct, display "correct guess"
# if lives count is >6 or if word is complete

import random
words = ['word', 'openai', 'google']


def hangman():
    lives = 6
    word = random.choice(words)# random word from list 
    print(word)
    random_word = ['_'] *len(word)
    # print(random_word)
    # guessed_letters = []
    wrong_letters = []

    while lives > 0 and '_' in random_word:
        print("\nWord: " + " ".join(random_word))
        print(f"Incorrect guesses: {', '.join(wrong_letters)}")
        print(f"Lives left: {lives}")
        guess = input("Guess a letter:").lower()
        
        if not guess.isalpha or len(guess) != 1:
            print("type one letter")
            continue
            
        # check if letter has already been guessed
        if guess in random_word or guess in wrong_letters:
            print("Already guessed this letter")
            continue
        # lives -= 1 #
        # guess_correctly = False
        # check for words with double letters
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    random_word[i] = guess
                print("You guessed right!")
        else:
            lives -= 1
            wrong_letters.append(guess)
            print("Incorrect guess!")
                # add input again
                
        if '_' not in random_word:
            print("Game over! You win")
            return
    if lives == 0:
        print("Game over, you lost")

hangman()