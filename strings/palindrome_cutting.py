def palindromeCutting(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if len(substring) > len(longest) and findPalindrome(substring):
                longest = substring

        s = s.replace(longest, "")
        if findPalindrome(s):
            substring = s[i:j+1]
            if len(substring) > len(longest) and findPalindrome(substring):
                longest = substring

    return s


def findPalindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


string = 'abaaac'

print(palindromeCutting(string))
