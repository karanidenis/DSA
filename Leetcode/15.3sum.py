#!/usr/bin/python3

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# def threeSum(nums):
#     """
#     set must not contain duplicate triplets
#     the triplets should add up to 0
#     """
#     triplets = set()
#     nums.sort()
#     for i in range(len(nums)):
#         for j in range(i +1, len(nums)):
#             for k in range(j + 1, len(nums)):
#                 triplet = (nums[i], nums[j], nums[k])
#                 # for triplet in triplets:
#                 if sum(triplet) == 0:
#                     triplets.add(triplet)
#                     triplets_list = list(triplets)
#     return triplets_list

# nums = [-1,0,1,2,-1,-4]
# print(threeSum(nums))

# def threeSum(nums):
#     """
#     set must not contain duplicate triplets
#     the triplets should add up to 0
#     shortest solution
#     """
#     nums.sort()
#     # triplets = set()
#     triplets = []
    # for i in range(len(nums)):
    #     if i > 0 and nums[i] == nums[i - 1]:
    #         continue
    #     l, r = i + 1, len(nums) - 1
    #     while l < r:
    #         s = nums[i] + nums[l] + nums[r]
    #         if s < 0:
    #             l += 1
    #         elif s > 0:
    #             r -= 1
    #         else:
    #             triplets.add((nums[i], nums[l], nums[r]))
    #             l += 1
    #             r -= 1
    # return triplets
#     for i in range(len(nums)):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         l, r = i + 1, len(nums) - 1
#         while l < r:
#             s = nums[i] + nums[l] + nums[r]
#             if s < 0:
#                 l += 1
#             elif s > 0:
#                 r -= 1
#             else:
#                 triplets.append([nums[i], nums[l], nums[r]])
#                 l += 1
#                 r -= 1
#     return triplets

# nums = [-1,0,1,2,-1,-4]
# # nums.sort()
# # print(nums) # [-4, -1, -1, 0, 1, 2]
# print(threeSum(nums))


# def Threesum(nums):
#     """
#     set must not contain duplicate triplets
#     the triplets should add up to 0
#     shortest solution
#     """
#     nums.sort()
#     triplets = []
#     for i in range(len(nums)):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         l, r = i + 1, len(nums) - 1
#         while l < r:
#             s = nums[i] + nums[l] + nums[r]
#             if s == 0:
#                 triplets.append([nums[i], nums[l], nums[r]])
#                 l += 1
#                 r -= 1
#                 while l < r and nums[l] == nums[l - 1]:
#                     l += 1
#                 while l < r and nums[r] == nums[r + 1]:
#                     r -= 1
#             elif s < 0:
#                 l += 1
#             else:
#                 r -= 1
#     return triplets


def three_sum(nums, target):
    nums.sort()  # Ensure the array is sorted
    result = []
    n = len(nums)
    
    # nums = [-1,0,1,2,-1,-4]  - [-1, -1, 0, 1, 2, 4]. n = 6
    # 0,1, 2, 3
    
    
    for i in range(n - 2):  # Loop through the array, leaving space for at least two more elements
        # Skip duplicate elements for the first element of the triplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1  # Set two pointers
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Move the left and right pointers to avoid duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
                
            elif current_sum < target:
                left += 1  # We need a larger sum
            else:
                right -= 1  # We need a smaller sum
    
    return result

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums, 1))
nums = [0,0,0,0]
print(three_sum(nums, 1))