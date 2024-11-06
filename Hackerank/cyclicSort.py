def cyclicSort(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return arr


arr = [3, 5, 2, 1, 4]
print(cyclicSort(arr))

# Amazon
def missingNumber(arr):
    i = 0
    n = len(arr)
    # while i < n:
    #     j = arr[i] - 1
    #     if arr[i] != arr[j]:
    #         arr[i], arr[j] = arr[j], arr[i]
    #     else:
    #         i += 1
    #     for i in range(n):
    #         if arr[i] != i + 1:
    #             return i + 1
    #         else:
    #             return -1
    
    # or
    
    i = 0
    n = len(arr)
    while i < n:
        j = arr[i]
        if arr[i] < n and arr[i] != i:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
        # return arr
    for i in range(n):
        if arr[i] != i:
            return i
        else:
            return n
            
        
arr = [3, 1, 2, 0, 4]  
print(missingNumber(arr))

# Google
# given an array nums of length n, nums[i] are in the range [1, n].
# return an array of all the numbers that are missing in nums that are in range [1, n]
def missingNums(arr):
    i = 0
    n = len(arr)
    while i < n:
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    print('arr', arr)
    missingNums = []
    for i in range(n):
        if arr[i] != i + 1:
            missingNums.append(i + 1)
    return missingNums 
    
arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(missingNums(arr))

# Ammazon
# given an array nums of length n+1, nums[i] are in the range [1, n].
# return the number that is duplicate
def duplicate(arr):
    i = 0
    n = len(arr)
    while i < n:
        j = arr[i] - 1
        if arr[i] != arr[j]: # [2, 3, 4, 5, 6] -> 2 != 3
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    print('duplicate:', arr)
    for i in range(n):
        if arr[i] != i + 1:
            return arr[i]
        

# arr = [1, 3, 4, 2, 2]
arr = [1, 1, 2]
print(duplicate(arr))
            
    
    
    
    