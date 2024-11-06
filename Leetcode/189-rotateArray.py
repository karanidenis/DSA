# Leetcode 189-rotate Array
# Given an array nums, rotate to the right by k steps.


def rotate(nums, k):
    # k = 3
    n = len(nums)
    k = k % n
    print(k)
    print(nums[n-k:])
    print(nums[:n-k])
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums

# or  

# def rotateArray(nums, k):
#     # use pointers to swap elements until k
#     n = len(nums)
#     j = n-1
#     # consider k
#     while k > 0:
#         # move all elements to the right, but the last one to the first
#         temp = nums[j]
#         # print(temp)
#         while j > 0:
#             nums[j] = nums[j-1]
#             j -= 1
#         nums[j] = temp       
#         k -= 1
#         j = n-1
#     return nums


nums =  [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums, k))
# print(rotateArray(nums, k))




