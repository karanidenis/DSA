# words list  > comp choice > random  >  
# word of underscores   > add letters to replace underscores
# lives > track count
# check for gameover > if no underscore left or lives end

import random

words = ['google', 'pareto', 'openai']

def playHangam():
    comp_choice = random.choice(words)
    
    player_word = ["_"] * len(comp_choice)
    wrong_guesses = []
    
    lives = 6
    
    while "_" in player_word and lives > 0:
        # print(f"\n{comp_choice} is correct word!")
        print("\nRemaining lives: ", lives)
        print(", ".join(player_word))
        print("Wrong guesses: ", ", ".join(wrong_guesses))
        # break
        
        guess = input("Enter a letter: ")
        
        if not guess.isalpha or len(guess) != 1:
            print("Enter one letter only!")
            continue
        
        if guess in wrong_guesses or guess in player_word:
            print("Already used this letter! try a different letter!")
            continue
        
        if guess in comp_choice:
            for i, letter in enumerate(comp_choice):
                if letter == guess:
                    player_word[i] = guess
                    print("Nice guess!")
        else:
            lives -= 1
            wrong_guesses.append(guess)
            print("Wrong guess!")
            
        
        


playHangam()
