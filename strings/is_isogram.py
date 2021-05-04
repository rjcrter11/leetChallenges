'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters 
is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
'''


def is_isogram(string):
    string.lower()

    for char in string:
        if string.count(char) > 1:
            return False
    return True


string = "Dermatoglyphics"

print(is_isogram(string))


def is_isogram_alt(string):
    return len(string) == len(set(string.lower()))


print(is_isogram_alt(string))
