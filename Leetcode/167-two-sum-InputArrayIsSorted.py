# Given a soted array numbers. - ascending order. Find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

def twoSum(numbers, t):
    n = len(numbers)
    i = 0
    j = n-1
    
    while i < j:
        if numbers[i] + numbers[j] == t:
            return [i+1, j+1]
        elif numbers[i] + numbers[j] < t:
            i += 1
        else:
            j -= 1
    # return [-1, -1]
    
    
numbers = [2, 7, 11, 15]
t = 9
print(twoSum(numbers, t)) # [1, 2]
    
    
    
    
    
    
    
    