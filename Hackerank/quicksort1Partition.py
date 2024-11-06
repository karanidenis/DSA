# Hackerank Quicksort 1 Partition
# Given a pivot arr[0], divide an array arr into 3, left= less than pivot, equal, right = greater than pivot. 

# examplearr = [5, 7, 4, 3, 8]
# pivot = 5
# left = [4, 3]
# right = [7, 8]
# arr = [4, 3, 5, 7, 8] or [3, 4, 5, 8, 7]


def quicksort(arr):
    p = arr[0]
    left = [i for i in arr[1:] if i < p]
    print(left)
    right = [i for i in arr[1:] if i > p]
    print(right)
    equal = [i for i in arr if i == p]
    print(equal)
    res = left + equal + right
    print(res)
    for i in res:
        print(i, end=" ")
    print()


arr = [4, 5, 3, 7, 2]
print(quicksort(arr))
    