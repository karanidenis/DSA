# CodeForces Segment with small sum
# Given array a1 of n ints. 
#  segement = [l...r] of a1 is a subarray such that 1 <= l <= r <= n. if sum of elements in segement is almost s, fins the longest good element.


def smallSumSegment(n, t, arr):
    n = len(arr)
    i = 0
    j = 0
    sum = 0
    ans = 0
    while j < n:
        sum += arr[j]
        # print(arr[j], sum)
        while sum > t:
            sum -= arr[i]
            # print(arr[i], arr[j], sum, j-i+1)
            i += 1
        ans = max(ans, j-i+1)
        j += 1
        
    return ans

# arr = [2, 6, 4, 3, 6, 8, 9]
# n = 7
# t = 20
n,t = map(int, input().split())
arr = list(map(int, input().split()))
print(smallSumSegment(n, t, arr)) # 4