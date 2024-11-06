# Codeforces pointers - Number of Smaller
# Given ints n and m, and n ints that make first array and m ints for 2nd array, find the number of elements in the first array that are smaller than the elements in the second array.

def numberOfSmaller(n, m, arr1, arr2):
    i = 0
    j = 0
    count = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            count += 1
            i += 1
        else:
            print(count, end=" ")
            j += 1
        
    while j < m:
        print(count, end=" ")
        j += 1
    print()

# n = 6
# m = 7
# arr1 = [1, 6, 9, 13, 18, 18]
# arr2 = [2, 3, 8, 13, 15, 21, 25]

n,m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
numberOfSmaller(n, m, arr1, arr2)
