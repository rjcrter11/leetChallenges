'''
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible 
number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is 
replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the 
same order and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".
'''


def lineEncoding(input):
    input += '0'
    result = ''
    count = ''
    consonant = ''

    for x in input:
        if x != consonant:
            if count == 1:
                result += consonant
            else:
                result += str(count) + consonant
            consonant = x
            count = 1
        else:
            count += 1
    return result


s = "aabbbc"

print(lineEncoding(s))
