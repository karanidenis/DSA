# Question 1:
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
 
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


# def sales(prices):
#     # sell - 
#     # or buy
    
#     # [7,1,5,3,6,4]
#     # [1,2,3,4,5]
    
#     n = len(prices)
    
#     profit = 0
#     for i, val in enumerate(prices):
#         # print(val)
#         y = i + 1
        
#         while y < n:
#             # if i > y and i == 0:
#             #     print("Can't buy because price is higher")
#             #     continue
            
#             if i < y:
#                 print(f"buy on day {i} and sell on day {y}")
#                 profit += prices[y] - prices[1]
            
#             # elif i == y:
#             #     print("same price")
#             #     continue
            
#             else:
#                 print("buy")
#                 # profit = 0
            
#             i += 1
#             y += 1
                
#     return profit


# prices = [7,1,5,3,6,4]
# print(sales(prices))



def sales(prices):
    n = len(prices)
    profit = 0
    
    for i in range(n-1):
        if prices[i] > prices[i + 1]:
            pass
            
        else:
            profit += prices[i + 1] - prices[i]
            
    return profit
  
prices = [7,1,5,3,6,4]

print(sales(prices))

prices = [7,7]
print(sales(prices))
