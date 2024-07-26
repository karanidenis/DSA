#!/bin/python3

import math
import os
import random
import re
import sys


def countingSort(arr):
    n = len(arr)
    max_val = max(arr)
    count = [0] * (max_val + 1)
    # print(count)
    for i in range(n):
        count[arr[i]] += 1
    print(f"{count} count1")
    for i in range(1, max_val + 1):
        y = i - 1
        count[i] += count[y]
    # print(f"{count} count2")
    output = [0] * n
    print(f"output: {output}") 
    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        # print(f"output: {output} arr[i]: {arr[i]} count[arr[i]]: {count[arr[i]]}")
        count[arr[i]] -= 1
    return output

if __name__ == '__main__':
    # n = 5

    # arr = [4, 3, 1, 2, 7]
    arr = [1,1,3,2,1]

    result = countingSort(arr)
    print(result)
