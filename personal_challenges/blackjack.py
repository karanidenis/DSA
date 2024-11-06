# Blackjack
# Create a Blackjack game with the following requirements:
# The player and the dealer are each dealt two cards.
# Allow the player to choose between "hit" (get another card) or "stand" (keep current hand).
# Display the player’s current score after each action.
# The dealer must follow the rule of standing on 17 or higher and hitting on less than 17.
# Determine the winner based on whose score is closer to 21 without going over.
# Display the final result (win, lose, or draw) after the game ends.

# have cards with values ✔
# have players - player and comp/dealer ✔
# allocate cards - 2 each at start, -1 incase they stand ✔
# check if decision is stand or hit ✔
# check winner - count total of both, 
# check if totals is > 21.
# check if dealer's total > 17, allow collect a card
# handle dealer and player turn

import random


def draw_cards(cards, num):
    random_cards = []
    for i in range(num):
        random_card = random.choice(cards)
        cards.remove(random_card)
        random_cards.append(random_card)
        
    return random_cards

# def handle_dealer_total(dealer, cards, new_cards):
#     dealer_total = check_total(dealer, cards)
    
#     if dealer_total > 21:
#         return -1
#     elif dealer_total >= 17:
#         return 0
#     else:
#         dealer.append(draw_cards(new_cards, 1))
#         print(dealer)
#         return 1
    
def check_total(player, cards_dict):
    total = 0
    for card in player:
        total += cards_dict[card]
    return total

# def handle_player_total(player, dealer, cards_dict):
#     player_total = check_total(player, cards_dict)
#     dealer_total = check_total(dealer, cards_dict)
#     if player_total > 21:
#         print("Dealer wins! your total is above 21")
#         return -1
#     if player_total < dealer_total:
#         return -2
#     else:
#         return 1
        

def playBlackjack():
    ranks = {
        'Two': 2,
        'Three': 3, 
        'Four': 4, 
        'Five': 5,
        'Six': 6, 
        'Seven': 7,
        'Eight': 8, 
        'Nine': 9, 
        'Ten': 10, 
        'Jack': 10, 
        'Queen': 10,
        'King': 10, 
        # 'Ace': [1, 11]
        'Ace': 11
    }
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    cards = {}
    for i, key in ranks.items():
        for j in suits:
            card = i + " of " + j
            cards[card] = key
    print(len(cards))
    # print(cards)
    
    cards_without_values = [key for key in cards.keys()]
    player = draw_cards(cards_without_values, 2)
    # print(player)

    dealer = draw_cards(cards_without_values, 2)
    print(dealer)
    
    print(len(cards_without_values))
    
    choices = {0: 'Stand', 1: 'Hit'}
    
    while True:
        print("One of Dealer's cards is ", dealer[0])
        print(f"Your cards are {player} and total is {check_total(player, cards)}")
        # break
    
        dealer_choice = random.randint(0, 1)
        print(dealer_choice)
        try:
            choice = int(input("Choose to hit or stand! Stand is 0 while Hit is 1: "))
        except ValueError:
            print("enter a number!")
            continue
        
        if choice not in range(2):
            print("Input 0 or 1 to Hit or Stand!")
            continue
        
        dealer_total = check_total(dealer, cards)
        player_total = check_total(player, cards)
        
        # if player decided to hit, compare totals and decide winner.
        # if player stands, dealer chooces to stand or hit, if dealer hits, they compare totals and decide winner else check dealer total then proceed
        
        if choice == 1:
            print("Player's total is ", player_total)
       
       
            
        
    
    
    
playBlackjack()