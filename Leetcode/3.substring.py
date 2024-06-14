strin = 'gthfgg'
lst = set()
for i in strin:
    lst.add(i)
print(lst)
s = ''.join(lst)
print(s)

# def get_unique_char_substrings(s):
#     unique_substrings = set()
#     n = len(s)
    
#     for i in range(n):
#         seen_chars = set()
#         substring = ""
#         for j in range(i, n):
#             if s[j] in seen_chars:
#                 break
#             seen_chars.add(s[j])
#             substring += s[j]
#             unique_substrings.add(substring)
    
#     return list(unique_substrings)

print()
s = 'abcabcbb'
uniq_sb = set()
n = len(s)
for i in range(n):
    seen_chars = set()
    s_str = ""
    for j in range(i, n):
        if s[j] in seen_chars:
            break
        seen_chars.add(s[j])
        s_str += s[j]
        uniq_sb.add(len(s_str))
print(uniq_sb)
print(max(uniq_sb))
# lens = []
# for stri in uniq_sb:
    # lens.append(len(stri))
# print(max(len(uniq_sb)))