# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]


def anagrams(arr):
  anagrams = []
  if len(arr) == 1:
    anagrams.append(arr)
    
  ang_dict = {}
  ang_list = []
  for word in arr:
    ang_dict[word] = [i for i in arr if sorted(i) == sorted(word)]  
    ang_list.append(ang_dict[word])
    
  unique_lists = [list(t) for t in {tuple(lst) for lst in ang_list}] 
  anagrams = unique_lists
  
  # print(ang_dict)
 
  return anagrams


strs = ["eat","tea","tan","ate","nat","bat"]
print(anagrams(strs))

strs = [""]
print(anagrams(strs))

strs = ["a"]
print(anagrams(strs))
