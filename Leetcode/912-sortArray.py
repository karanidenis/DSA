# Leetcode 912. Sort in Ascending Order

# Given an array of integers nums, sort the array in ascending order.
# use time complexity O(nlogn) and space complexity O(1)

def sortArray(nums):
    def mergeSort(nums, low, high):
        if low >= high:
            return
        
        mid = (low + high) // 2
        mergeSort(nums, low, mid)
        mergeSort(nums, mid + 1, high)
        
        i = low
        j = mid + 1
        temp = []
        
        while i <= mid and j <= high:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        
        while i <= mid:
            temp.append(nums[i])
            i += 1
        
        while j <= high:
            temp.append(nums[j])
            j += 1
        
        nums[low:high + 1] = temp
    
    mergeSort(nums, 0, len(nums) - 1)
    return nums


# Time complexity: O(nlogn)
# Space complexity: O(1)
# Test cases
# [5,2,3,1] -> [1,2,3,5]
# [5,1,1,2,0,0] -> [0,0,1,1,2,5]
nums = [5,2,3,1]
print(sortArray(nums))
nums = [5,1,1,2,0,0]
print(sortArray(nums))