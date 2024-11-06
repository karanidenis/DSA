# Hackerank Ruuning time of  Algorithms

# Running time of algorthms depends on no. of operations executted. The more the no. of opertaions the more the running time. 
# We want to know how many operations an algorithm wiill execute in proportion to the size of the size of its input. 

# Fror each element v in array N, insertion sort compares the no. to those to its left until reaches a lower value element or the start. 

# chllenge, for an insertion sort, keep track of the no. of shifts it makes while sorting. Shift occurs when an element's position changes in the arrays. 


def insertionSort(arr):
    n = len(arr)
    count = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            count += 1
            j -= 1
            print(arr, count)
        arr[j+1] = key
    return arr
            

arr = [2, 1, 3, 1, 2]
# arr = [4, 3, 2, 1]
print(arr)
print(insertionSort(arr))
    