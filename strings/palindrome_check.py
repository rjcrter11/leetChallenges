'''
Write a function that takes in a non-empty string and that returns a boolean
representing whether the string is a palindrome

string = 'abcdcba'
ouput = true
'''


def palindrome(str):
    left = 0
    right = len(str)-1

    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True


string = 'abcdcba'
result = palindrome(string)
print(result)
