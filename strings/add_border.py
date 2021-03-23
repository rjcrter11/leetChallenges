'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]

'''


def addBorder(picture):
    return ['*' * (len(picture[0])+2)] + ['*' + i + '*' for i in picture] + ['*' * (len(picture[0])+2)]


picture = ["abc",
           "ded"]

print(addBorder(picture))
