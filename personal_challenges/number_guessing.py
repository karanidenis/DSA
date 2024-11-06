# 4. Number Guessing Game
# Create a Number Guessing game with the following requirements:
# The computer selects a random number between 1 and 100.
# The player inputs guesses, and the computer provides feedback (higher/lower).
# Keep track of the number of guesses the player makes.
# End the game when the player guesses the correct number.
# Display a congratulatory message and the total number of guesses made.



# play game function
# comp choose a random no
# user input
# check is guess is lower or higher
# print whether to go higher or lower + count guesses
# check if if guess is correct, finish game

import random

def check_equal(guess, comp_choice):
    if guess == comp_choice:
        return 0
    elif guess > comp_choice:
        return -1
    else:
        return 1

def playGame():
    # let comp chooce a number
    comp_choice = random.randint(0, 100)
    print(comp_choice)
    guesses = 0
    
    while True:
        # allow player to guess
        try:
            guess = int(input("Guess a number between 0 - 100: "))
        except ValueError:
            print("Input a number!")
            continue
        
        if guess > 0 and guess <= 100:            
            # check if less or greater
            res = check_equal(guess, comp_choice)
            if res == 0:
                guesses += 1
                print("Congratulations! number was ", comp_choice)
                print(f"You tried {guesses} times!")
                break
            elif res == 1:
                print("Guess a higher value!")
                guesses += 1
                continue
            else:
                print("Guess a lower value!")
                guesses += 1
                continue
        print("Input a value between 0 - 100")
        continue
    
        
playGame()