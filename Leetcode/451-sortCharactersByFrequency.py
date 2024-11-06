# Leetcode 451. Sort Characters By Frequency
# given string s. sort the string by the frequency of characters in descending order

def frequencySort(s):
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    print(freq)
    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
    print(freq)
    result = ''
    for k, v in freq.items():
        result += k * v
        
    return result

s = "tree"
print(frequencySort(s))
s = "cccaaa"
print(frequencySort(s))
s = "Aabb"
print(frequencySort(s))