'''
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
'''


def longest_digits_prefix(input):
    prefix = ""

    for x in input:
        if x.isdigit():
            prefix += x
        if not x.isdigit():
            break
    return prefix


inputString = "123aa1"
print(longest_digits_prefix(inputString))
