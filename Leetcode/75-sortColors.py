# Leetcode 75.sort Colors
# given array nums. 
# n - red - 0, white - 1 / blue - 2. 
# sort them n items such that same color are adjacent. 

def sortColors(nums):
    n = len(nums)
    freq = {0:0, 1:0, 2:0}
    
    for i in nums:
        freq[i] += 1
        
    print(freq)
    i =0

    for key in range(n):
        for _ in range(freq[key]):
            nums[i] = key
            i += 1    
            print(nums)
        
            
        
    
    
    
# nums = [2,0,2,1,1,0]
# nums = [2, 0, 1]
nums = [0]
print(sortColors(nums))