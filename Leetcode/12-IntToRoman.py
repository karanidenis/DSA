#!/usr/bin/env python3
# Seven different symbols represent Roman numerals with the following values:

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
# Given an integer, convert it to a Roman numeral.
# Example 1:

# Input: num = 3749

# Output: "MMMDCCXLIX"

# Explanation:

# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
# Example 2:

# Input: num = 58

# Output: "LVIII"

# Explanation:

# 50 = L
#  8 = VIII
# Example 3:

# Input: num = 1994

# Output: "MCMXCIV"

# Explanation:

# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV


# def intToRoman(num):
#     num = str(num)
#     vals = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
#     val = ''
#     for i, digit in enumerate(num):
#         scale = 10 ** (len(num) -i -1)
#         value = int(digit) * scale
#         if value in vals:
#             val += vals[value]
#             print(f"{i}.{digit} - {value}-{val}")
#         else:
#             while value > 0:
#                 for k in sorted(vals.keys(), reverse=True):
#                     while value >= k:
#                             val += vals[k]
#                             value -= k
#                             print(f"Adding {vals[k]} for value {k}, remaining {value}")
#     return val


def intToRoman(num):
    num_str = str(num)
    length = len(num_str)
    val = ''
    vals = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    for i, digit in enumerate(num_str):
        scale = 10 ** (length - i - 1)
        digit = int(digit)
        if digit == 0:
            continue
        if digit == 9:
            val += vals[1 * scale] + vals[10 * scale]
        elif digit >= 5:
            val += vals[5 * scale] + vals[1 * scale] * (digit - 5)
        elif digit == 4:
            val += vals[1 * scale] + vals[5 * scale]
        else:
            val += vals[1 * scale] * digit
    return val

# n = 1000
# print(intToRoman(1143))  # MCXLIII
# print(intToRoman(2897))  #MMDCCCXCVII
# print(intToRoman(3749))  # MMMDCCXLIX
print(intToRoman(70))  # LXX
# print(intToRoman(1994))  # MCMXCIV