'''
Given a string, your task is to replace each of its characters by 
the next one in the English alphabet; i.e. replace a with b, 
replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should 
be alphabeticShift(inputString) = "dsbaz".
'''


def alphabeticShift(input):
    new_letters = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    for letter in input:
        new_letter_code = alphabet.index(letter) + 1
        new_letters.append(alphabet[new_letter_code % 26])

    return "".join(new_letters)


inputString = "crazy"
print(alphabeticShift(inputString))
