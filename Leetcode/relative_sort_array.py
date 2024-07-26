# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
arrs = []
match_arrs = []
for i in arr2:
    matching_nums = list(filter(lambda x:x == i, arr1))
    match_arrs.append(matching_nums)
print(match_arrs)
new_arr = [i for arr in match_arrs for i in arr]
print(new_arr)

others = [num for num in arr1 if num not in new_arr]
print(sorted(others))
new_arr.extend(others)
print(new_arr)

