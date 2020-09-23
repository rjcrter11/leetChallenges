'''Given a string, we can "shift" each of its letter to its successive letter, 
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, 
group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''

from collections import defaultdict


def groupStrings(strings):
    def diff(s): return tuple((ord(a) - ord(b)) % 26 for a, b in zip(s, s[1:]))
    d = defaultdict(list)
    for s in strings:
        d[diff(s)].append(s)
    return d.values()


strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

print(groupStrings(strings))
