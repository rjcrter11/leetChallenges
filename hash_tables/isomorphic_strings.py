'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''


def isIsomorphic(s, t):

    ds = {}
    dt = {}
    for x in range(len(s)):
        ds[x] = x
        dt[x] = x

    arr1 = [ds[key] for key in ds]
    arr2 = [dt[key] for key in dt]

    return arr1 == arr2


string1 = "ab"
string2 = "aa"

print(isIsomorphic(string1, string2))
