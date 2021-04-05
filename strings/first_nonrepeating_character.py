'''
Write a function that takes in a string of lowercase English 
alphabet letters and returns the index of the string's first non-repeating
character.

sample output:
string = 'abcdcaf'

sample output:
1
'''


def firstNonRepeatingCharacter(string):
    # Write your code here.

    d = {}

    for x in string:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    for i in range(len(string)):
        if d[string[i]] == 1:
            return i
    return -1


string = 'abcdcaf'
print(firstNonRepeatingCharacter(string))
