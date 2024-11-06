# Leetcode 1561. Maximum Number of Coins You Can Get
# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
# In each step, you will choose any 3 piles of coins (not necessarily consecutive).
# Of your choice, Alice will pick the pile with the maximum number of coins.
# You will pick the next pile with maximum number of coins.
# Your friend Bob will pick the last pile.

# Repeat this procedure until there are no more piles of coins.

# Given an array of integers piles where piles[i] is the number of coins in the ith pile.

# Return the maximum number of coins which you can have.


# def maxCoins(pile):
#     alice = []
#     you = []
#     bob = []
#     pile = sorted(pile, reverse=True)
#     print(pile)
#     round = 1
#     while pile:
#         batch = pile[:3]
#         you.append(batch[1])
#         pile = pile[3:]
#         round += 1
#     print(you)
#     return sum(you)

# or 

def maxCoins(pile):
    n = len(pile) // 3
    pile = sorted(pile, reverse=True)
    total = 0
    for i in range(1, 2*n, 2):
        total += pile[i]
        print(i)
        
    return total
        
        
        
pile = [2, 6, 5]
print(maxCoins(pile))
pile = [9, 8, 7, 6, 5, 1, 2, 3, 4]
print(maxCoins(pile))  # 15 instead of 18 ??
pile = [2, 4, 1, 2, 7, 8]
print(maxCoins(pile))