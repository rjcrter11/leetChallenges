'''
You're given an array of integers and an integer. Write a function that
moves all instances of that integer in the array end of the array and
returns the array.
The function should perform this in place and doesn't need to maintain
the order of the other integers.

array = [2,1,2,2,2,3,4,2]
output = [1,3,4,2,2,2,2,2]

'''


def moveElementToEnd(array, toMove):
    left = 0

    right = len(array) - 1

    while left < right:
        if array[left] != toMove:
            left += 1
        elif array[right] == toMove:
            right -= 1
        else:
            array[left], array[right] = array[right], array[left]
    return array
