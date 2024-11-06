#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, n):
        y = arr[i]
        j = i - 1
        while j >= 0 and  arr[j] > y:
            arr[j + 1] = arr[j]
            j -= 1
            print(*arr)
        arr[j + 1] = y
    print(*arr)


if __name__ == '__main__':
    # n = int(input().strip())
    n = 10

    # arr = list(map(int, input().rstrip().split()))
    arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

    insertionSort1(n, arr)
