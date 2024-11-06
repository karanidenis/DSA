#  Codeforces Pointers - Number of Equal
# Given 2 arrays, a,b, sorted in ascending order. Find number of pairs (i,j) for which a[i] == b[j].

def numberOfEqual(n, m, arr1, arr2):
    i = 0
    j = 0
    count = 0
    while i < n and j < m:
        if arr1[i] == arr2[j]:
            count1 = 0
            val1 = arr1[i]
            while i < n and arr1[i] == val1:
                count1 += 1
                i += 1
            count2 = 0
            val2 = arr2[j]
            while j < m and arr2[j] == val2:
                count2 += 1
                j += 1
            
            count += count1 * count2
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
        
    return count


# n = 8
# m = 7
# arr1 = [1, 1, 3, 3, 3, 5, 8, 8]
# arr2 = [1, 3, 3, 4, 5, 5, 5]
n,m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(numberOfEqual(n,m, arr1, arr2))