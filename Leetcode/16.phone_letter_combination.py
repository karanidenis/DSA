#!/usr/bin/python3

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# input: digits = "23"
# output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# input: digits = ""
# output: []

# Example 3:
# input: digits = "2"
# output: ["a","b","c"]

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(" ".join(path))
            return
        for letter in phone[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    combinations = []
    backtrack(0, [])
    return combinations

digits = "23"
print(letterCombinations(digits))
digits = "2"
print(letterCombinations(digits))
