# Leetcode 283
# Give array nums. move all 0s to end of it. maintain order of non-zero ints.
# Don't make a copy of array.

def moveZeroes(nums):
    n = len(nums)
    non_zero_ind = 0
    for i in range(n):
        if nums[i] != 0:
            nums[non_zero_ind] = nums[i]
            non_zero_ind += 1
    print(nums)    
    for i in range(non_zero_ind, n):
        nums[i] = 0
    return nums
        
nums = [0,1,0,3,12]
print(moveZeroes(nums))
