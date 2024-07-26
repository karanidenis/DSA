# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

# nums = [2, 0, 1]
nums = [2,0,2,1,1,0]
print(nums)
start = 0
pivot = nums[start]

if len(nums) > 0:
    while start + 1 < len(nums):
        next = nums[start + 1]
        if pivot > next:
            print(f'Pivot {pivot}')
            print(f'next  {next}')
            nums[start], nums[start + 1] = nums[start + 1], nums[start]
        start += 1

print(nums)

# nums = [2,0,2,1,1,0]
nums = [2, 0, 1]
print(nums)
end = len(nums) -1
pivot = nums[end]

while end - 1 > 0:
    next = nums[end - 1]
    if pivot < next:
        print(f'Pivot {pivot}')
        print(f'next  {next}')
        nums[end - 1], nums[end] = nums[end], nums[end -1]
    end -= 1

print(f"nums: {nums}")