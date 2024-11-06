# Leetcode 18 - 4Sum
# Given array nums of n ints, return array of all unique quadruplets such that:
# 0 <= a, b, c, d < n & a + b + c + d == target

# eg
# nums = [1, 0, -1, 0, -2, 2] target = 0.
# answ: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

def fourSum(nums, target):
    n = len(nums)
    # nums = sorted(nums) # [-2, -1, 0, 0, 1, 2]
    nums.sort()
    # i = 0
    # j = i + 1
    quad = []
    for i in range(n):
        for j in range(i + 1, n):
            left = j + 1
            right = n - 1
            while left < right:
                sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                
                if sum_ == target:
                    lst =  [nums[i], nums[j], nums[left], nums[right]]
                    quad += lst
                    # print([nums[i], nums[j], nums[left], nums[right]])
                    # print(quad)
                    # return quad 
                    
                elif sum_ < target:
                    left += 1
                else:
                    right -= 1
    return quad
        

sum = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(sum, target))