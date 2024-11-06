# Hackerank Fraudulent Activity Notifications

# Hackraank bank has a policy to notify clients when the amount of a transaction is greater than or equal to 2x the median of the previous d transactions. The bank has a list of transactions in chronological order. Each transaction is a non-negative integer. Determine the number of notifications the clients will receive.

# Example
# expenditure = [10, 20, 30, 40, 50], d = 3, 
# The median of the previous d transactions is 20. The next transaction is 40. The client receives a notification because 40 >= 2*20.
# median on day 5 is 30. The next transaction is 50. The client doesnt receive a notification because 50 < 2*30.

# [2, 4, 6, 7] med = 4 + 6 = 10/2 = 5
# [4, 5, 7] med = 5

def activityNotifications(expe, d):
    n = len(expe)
    # expe = sorted(expe)
    notifications = 0
    # j = d
    for j in range(d, n):
        transcs = sorted(expe[j-d:j])
        print(transcs)
        if d % 2 == 1:
            median = transcs[d // 2]
        else:
            median = (transcs[d // 2] + transcs[d // 2 - 1]) / 2
        # i += 1
        print(median)
        
        if expe[j] >= 2 * median:
            # print(expe[j], 2*median)
            notifications += 1
        print(expe[j], 2*median)
    print("Notifications:", notifications)
        

# expe = [10, 20, 30, 40, 50, 60]
expe = [2, 3, 4, 2, 3, 6, 8, 4, 5]
# print(sorted(expe))
d = 5
# n = 5
activityNotifications(expe, d)