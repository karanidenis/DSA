# Leetcode
# Given an array nums. length n, nums[i] are iin range [1, n].
# find ints that appear twice
# algorithm should run in 0(n) time.


def duplicates(nums):
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    print(nums)
    duplicates = []
    for i in range(n):
        if nums[i] != i + 1:
            duplicates.append(nums[i])
            # print(duplicates)
        # else:
        #     return []
    return duplicates
        
    
# nums = [4,3,2,7,8,2,3,1]
# nums = [1, 1, 2]
nums = [1]
print(duplicates(nums))