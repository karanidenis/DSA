# CodeForces 479 Less or Equal

# given n integers and k, 
# find x which is: bigger/equal to k numbers in n

def lessOrEqual(n, k):
    # nums = list(map(int, input().split()))
    n.sort()
    if k == 0:
        if n[0] == 1:
            return -1
        return 1
    if k == len(n):
        return n[-1]
    if n[k - 1] == n[k]:
        return -1
    return n[k - 1]


# nums = [3, 7, 5, 1, 10, 3]
# print(lessOrEqual(nums, 4))

# Reading the input
n, k = map(int, input().split())  # Input size n and k
nums = list(map(int, input().split()))  # List of n integers
# Output the result
print(lessOrEqual(nums, k))