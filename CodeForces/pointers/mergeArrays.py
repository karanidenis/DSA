# Codeforces Pointers - merging arrays
# Given 2 arrays, sorted in non-decreasing order. Merge them in non-decreasing order without using extra space.

def mergeArrays(n, m, arr1, arr2):
    # n = len(arr1)
    # m = len(arr2)
    i = 0
    j = 0
    # res = []
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            print(arr1[i], end=" ")
            # res.append(arr1[i])
            i += 1
        else:
            print(arr2[j], end=" ")
            # res.append(arr2[j])
            j += 1
    while i < n:
        print(arr1[i], end=" ")
        # res.append(arr1[i])
        i += 1
    while j < m:
        print(arr2[j], end=" ")
        # res.append(arr2[j])
        j += 1
    print()
    # return res
    
    
# arr1 = [1, 6, 9, 13, 18, 18]
# arr2 = [2, 3, 8, 13, 15, 21, 25]
# print(mergeArrays(arr1, arr2))

n, m = map(int, input().split())  # Input size n and k
nums_n = list(map(int, input().split()))  # List of n integers
nums_m = list(map(int, input().split()))  # List of n integers
# print(mergeArrays(n, m, nums_n, nums_m))
mergeArrays(n, m, nums_n, nums_m)
