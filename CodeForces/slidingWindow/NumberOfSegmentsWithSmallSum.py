# CodeForces Segment with small sum
# Given array a1 of n ints. 
#  segement = [l...r] of a1 is a subarray such that 1 <= l <= r <= n. if sum of elements in segement is almost s, find the number/sum closest to target.

def segmentSumWithSmallSum(n, t, arr):
    i = 0
    count = 0
    sum = 0
    for j in range(n):
        sum += arr[j]
        
        while sum > t:
            sum -= arr[i]
            i += 1
    
        count += (j - i + 1)
    return count


n, t = map(int, input().split())
arr = list(map(int, input().split()))
# n = 7
# t = 20
# arr = [2,6, 4, 3, 6, 8, 9]
print(segmentSumWithSmallSum(n, t, arr))