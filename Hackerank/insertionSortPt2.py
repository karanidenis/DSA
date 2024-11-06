# Hackerank: Insertion Sort - Part 2
# Given array a1 of n ints.

def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(*arr)
        
n = 7
arr = [3, 4, 7, 5, 6, 2, 1]
insertionSort2(n, arr)