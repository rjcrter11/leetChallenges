'''
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].


'''


def allLongestStrings(input):
    output = []
    max_len = 0

    if len(input) == 1:
        return input

    for i in range(len(input)):
        char_len = len(input[i])
        max_len = max(char_len, max_len)

    for char in input:
        if len(char) == max_len:
            output.append(char)

    return output


inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(inputArray))


def longestStringsAlt(input):
    maximum = max(len(s) for s in input)
    result = [s for s in input if len(s) == maximum]
    return result


print(longestStringsAlt(inputArray))
