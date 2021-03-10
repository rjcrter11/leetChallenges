'''
Write a function that, given a string, returns its longest palindromic substring.

input = "abaxyzzyxf"
output = xyzzyx
'''


def palindromicSubstring(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if len(substring) > len(longest) and findPalindrome(substring):
                longest = substring
    return longest


def findPalindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


input = "abaxyzzyxf"

print(palindromicSubstring(input))
