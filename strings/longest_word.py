'''
Define a word as a sequence of consecutive English letters. 
Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".
'''


def longestWord(text):
    count = 0
    res = ""
    result = []
    new_result = [None] * 1

    for x in text:
        if x.isalpha():
            res += x
            result.append(res)
        else:
            res = ""

    for x in result:
        if len(x) > count:
            count = len(x)
            new_result[0] = x

    return new_result[0]


text = "Ready, steady, go!"
print(longestWord(text))
