#!usr/bin/python3

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) -1
    a[mid], a[n-1] = a[n-1], a[mid]
    print(a)
    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1
        print(a)
    # a[1], a[n-1] = a[n-1], a[1]
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

# test_cases = int(input())
# for cs in range (test_cases):
    # n = int(input())
    # a = list(map(int, input().split()))
    
# def findZigZagSequence(a, n):
#     a.sort()
#     mid = int((n + 1)/2)
#     i = a[0]
#     first = a[1:mid]
#     second = a[mid:n]
#     r_first = first[::-1]
#     print(first)
#     print(r_first)
#     print(second)
#     print(i + r_first + second)
 
n = 7
a = [2, 3, 5, 1, 4, 6, 7]
findZigZagSequence(a, n)



