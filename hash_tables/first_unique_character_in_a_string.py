'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.
'''

from collections import Counter


def firstUniqueChar(s):
    count = Counter(s)

    print(count)

    for idx, x in enumerate(s):
        if count[x] == 1:
            return idx
    return -1


string = "loveleetcode"

print(firstUniqueChar(string))
