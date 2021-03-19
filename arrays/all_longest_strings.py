'''
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
'''


def allLongestStrings(arr):
    max_len = 0
    output = []

    for chars in arr:
        max_len = max(len(chars), max_len)

    for char in arr:
        if len(char) == max_len:
            output.append(char)

    return output


def longestStringsListComp(arr):
    max_len = max(len(string) for string in arr)
    output = [string for string in arr if len(string) == max_len]
    return output


inputArray = ["aba", "aa", "ad", "vcd", "aba"]

print(allLongestStrings(inputArray))
