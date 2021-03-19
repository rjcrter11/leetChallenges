'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.
'''


def commonCharacterCount(s1, s2):
    count = 0
    common_chars = set(s1) & set(s2)

    for x in common_chars:
        count += min(s1.count(x), s2.count(x))
    return count


s1 = "aabcc"
s2 = "adcaa"

print(commonCharacterCount(s1, s2))
