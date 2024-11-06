#!usr/bin/python3

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


# def longestCommonPrefix(s):
#     if not s:
#         return ""
#     n = len(s)
#     final_str = ""
#     s.sort()
#     print(s)
#     first = s[0]
#     last = s[n-1]
#     i = 0
#     while i < len(first) and i < len(last):
#         if first[i] == last[i]:
#             final_str += first[i]
#         else:
#             break
#         i += 1
#     return final_str

# strs = ["flower","flow","flight"]
# print(longestCommonPrefix(strs)) #fl

# strs = ["dog","racecar","car"]
# print(longestCommonPrefix(strs)) #""

def longestCommonPrefix(s):
    if not s or len(s) == 0:
        return ""
    s.sort()
    print(s)
    for i in range(len(s[0])):
        if s[0][i] != s[-1][i]:
            return s[0][:i]
    return s[0]

strs = ["a"]
print(longestCommonPrefix(strs)) #a
print(strs[-1][:1]) #a

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs)) #fl
print(strs[0][:2]) #fl

strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs)) #""
print(strs[0][:2]) #do