# Hackerank Correctness and Loop Invariant
 
def insertion_sort(m, l):
    for i in range(1, m):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
    # print(*l)

# m = int(input().strip())
# ar = [int(i) for i in input().strip().split()]
ar = [7, 4, 3, 5, 6, 2]
insertion_sort(ar)
print(" ".join(map(str,ar)))