# Leetcode 493 Reverse-pairs

# Given an array nums. return reverse pairs in nums (i, j),
# 0 <= i < j < n and nums[i] > 2 * nums[j]

def reversePairs(nums):
    def mergeSort(nums, low, high):
        if low >= high:
            return 0
        
        mid = (low + high) //2
        count = mergeSort(nums, low, mid) + mergeSort(nums, mid+1, high)
        # print(count)
        
        j = mid + 1
        for i in range(low, mid + 1):
            while j <= high and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)
        
        # merge
        nums[low:high + 1] = sorted(nums[low:high + 1])
        return count
    
    return mergeSort(nums, 0, len(nums) - 1)
        
    # n = len(nums)
    # low = 0
    # high = n
    # mid = len(nums) // 2
    
    # result = []
    # i = j = 0
    # left = nums[:mid]
    # print(left)
    # right = nums[mid:]
    # print(right)

    # while i < len(left) and j < len(right):
    #     if left[i] < right[j]:
    #         result.append(left[i])
    #         i += 1
    #     else:
    #         result.append(right[j])
    #         j += 1

    # result.extend(left[i:])
    # result.extend(right[j:])

    # return result
    
    
    # if len(nums) <= 1:
    #     return nums

    # mid = len(nums) // 2
    # leftHalf = nums[:mid]
    # rightHalf = nums[mid:]

    # sortedLeft = reversePairs(leftHalf)
    # sortedRight = reversePairs(rightHalf)
    
    # print('sortedRight:', sortedRight)
    # print(sortedLeft)
    # return 1
    

nums = [1,3,2,3,1]
print(reversePairs(nums))