# interview prep using a game

# Rock, paper, Scissors
# user chooses either rock, paper, scissors [0, 1, 2]
# computer chooses either [0, 1, 2]
# rock wins against scissors, looses against paper
# scissors win against paper, loose against rock
# paper win against rock, loose against scissors
# check what user picks, check what comp picks, decide winner.
# play three times, highest wins win

import random

values = ['rock', 'paper', 'scissors']
options = [0, 1, 2]


def playGame():
    """
    rock - 0 > scissors < paper
    paper - 1 > rock < scissors
    scissors - 2 > paper < scissors
    
    """
    count = 0
    plays = 3
    my_wins = 0
    comp_wins = 0
    ties = 0
    while count <= plays:
        comp_choice = random.choice(options)
        print(f"Computer picked: {values[comp_choice]}")
        user_choice = int(input("select value between 0 - 2. /n 0 for rock, /n 1 for paper, 2 for scissors: "))
        
        if user_choice not in options:
            print("Invalid choice. Please choose 0, 1, or 2.")
            continue
        print(f"You picked: {values[user_choice]}")
        
        # Determine the winner using a scoring system
        result = (user_choice - comp_choice) % 3
        # 0 rock + 0 rock -> tie
        # 0 rock + 
        plays -= 1
        print(f"{plays} more plays")
        
        if result == 0:
            # print("You tie!")
            ties += 1
        elif result == 1:
            # print("You win")
            my_wins += 1
        else:
            # print("Comp Win!")
            comp_wins += 1

        if plays == 0:
            if my_wins > comp_wins:
                print("You win!")
            elif comp_wins > my_wins:
                print("Comp wins!")
            else:
                print("You tie")
            break
            
         
            
playGame()
        
        
# print(0%3) = 0
# print(-1%3) = 2
# print(-2%3)
# print(1%3)
# print(0%3)
# print(-1%3)
# print(2%3)