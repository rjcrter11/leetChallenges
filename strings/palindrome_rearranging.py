'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
'''


def palindromeRearranging(string):
    l = list(string)
    chars = set(l)

    counts = sum([l.count(x) % 2 for x in chars])

    return counts <= 1


inputString = "aabb"
print(palindromeRearranging(inputString))
