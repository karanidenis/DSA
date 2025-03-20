# QUESTION:

# You are given an array of strings. Your task is to transform each string in the array based on the following rules:
# If the length of the string is even, reverse the string.
# If the length of the string is odd, convert the string to uppercase.
# After performing the transformations, return a new array containing the modified strings.

# Function Signature:
# def transformString

# Eg:

# strings = ["hello", "world", "code", "interview"]
# Output:  ["HELLO", "WORLD", "edoc", "INTERVIEW"]


def stringTransformation(arr):
    new_strings = []
    
    
    for word in arr:
        length = len(word)
        if length % 2 == 0:
            word = word[::-1]               
        else:
            word = word.upper()
            
        new_strings.append(word)
        
    return new_strings
            

strings = ["hello", "world", "code", "interview"]
print(stringTransformation(strings))