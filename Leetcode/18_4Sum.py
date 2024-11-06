# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

# def four_sum(nums, target):
#     nums.sort() # [-2, -1, 0, 0, 1, 2] 
#     def k_sum(nums, target, k):
#         res = []
#         if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
#             return res
#         if k == 2:
#             return two_sum(nums, target)
#         for i in range(len(nums)):
#             if i == 0 or nums[i - 1] != nums[i]:
#                 for subset in k_sum(nums[i + 1:], target - nums[i], k - 1):
#                     res.append([nums[i]] + subset)
#         return res
#     def two_sum(nums, target):
#         res = []
#         lo, hi = 0, len(nums) - 1
#         while lo < hi:
#             sum_ = nums[lo] + nums[hi]
#             if sum_ < target or (lo > 0 and nums[lo] == nums[lo - 1]):
#                 lo += 1
#             elif sum_ > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
#                 hi -= 1
#             else:
#                 res.append([nums[lo], nums[hi]])
#                 lo += 1
#                 hi -= 1
#         return res
#     return k_sum(nums, target, 4)

def four_sum(nums, target):
    nums.sort()
    # return quadruplets
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            left = j + 1
            right = len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                if sum_ == target:
                    return([nums[i], nums[j], nums[left], nums[right]])
                elif sum_ < target:
                    left += 1
                else:
                    right -= 1
    return res

# [-2, -1, 0, 0, 1, 2]
nums = [1,0,-1,0,-2,2]
print(four_sum(nums, 0))

# nums = [2,2,2,2,2]
# print(four_sum(nums, 8))

# nums = [0,0,0,0]
# print(four_sum(nums, 0))