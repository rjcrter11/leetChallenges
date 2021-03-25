'''
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
'''


def arrayReplace(arr, elemToReplace, substitutionElem):
    return [substitutionElem if num == elemToReplace else num for num in arr]


inputArray = [1, 2, 1]
elemToReplace = 1
substitutionElem = 3
print(arrayReplace(inputArray, elemToReplace, substitutionElem))
