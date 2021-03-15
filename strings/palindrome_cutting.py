def palindromeCutting(s):
    longest = ""
    hasPal = True
    stringLen = len(s)
    print(stringLen)
    while hasPal:
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if len(substring) > len(longest) and findPalindrome(substring):
                    longest = substring
                s = s.replace(longest, "")
            print(s)

            if not findPalindrome(s):
                print('length', len(s))
                hasPal = False

        # s = s.replace(longest, "")
        # if findPalindrome(s):
        #     substring = s[i:j+1]
        #     if len(substring) > len(longest) and findPalindrome(substring):

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


string = 'jkjabacodoc'

print(palindromeCutting(string))
