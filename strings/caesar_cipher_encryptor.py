'''
Given a non-empty string of lowercase letters and a not-negative integer 
representing a key, write a function that returns a new string obtained by
shifting every letter in the input string by k positions in the alphabet, where
k is the key. 
Note that letters should 'wrap' around the alphabeet; in other words, the letter
z shifted by one returns the letter a

string = "xyz"
key = 2

output = "zab"
'''


def caesar(string, key):
    newLetters = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    for letter in string:
        newLetterCode = alphabet.index(letter) + key
        newLetters.append(alphabet[newLetterCode % 26])

    return "".join(newLetters)


string = "xyz"
key = 2

print(caesar(string, key))
