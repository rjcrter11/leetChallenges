'''
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''


def groupAnagrams(strs):
    result = {}

    for i in strs:

        x = ''.join(sorted(i))
        print(x)
        if x not in result:
            result[x] = [i]
        else:
            result[x].append(i)
    print(result)
    return result.values()


input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(input_strings))
