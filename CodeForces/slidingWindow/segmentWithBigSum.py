# CodeForces Segment with small sum
# Given array a1 of n ints. 
#  segement = [l...r] of a1 is a subarray such that 1 <= l <= r <= n. if sum of elements in segement is almost s, fins the shortest good element.

def bigSumSegment(n, t, arr):
    i = 0
    # j = 0
    ans = float('inf')
    sum = 0
    for j in range(n):
        sum += arr[j]
        
        while sum >= t:
            sum -= arr[i]
            # print(arr[i], arr[j], sum, j-i)
            ans = min(ans, j - i + 1)
            i += 1
        
    return ans if ans !=  float('inf') else -1


# arr = [2, 6, 4, 3, 6, 8, 9]
# n = 7
# t = 20
n, t = map(int, input().split())
arr = list(map(int, input().split()))
print(bigSumSegment(n,t,arr))