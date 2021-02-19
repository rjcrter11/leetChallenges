'''
Given an array of integers between 1 and n, inclusive, where n is the len of the array,
write a function that returns the first integer that appears more than once(when the 
array is read from left to right).
In other words, out of all the integers that might ocur more than once in the input array
your function should return the one whose first duplicate value has the minimum index.
If no integer appears more than once, your function should return -1

array = [2,1,5,2,3,3,4]
output = 2
'''


def firstDuplicate(array):
    seen = set()

    for val in array:
        if val in seen:
            return val
        seen.add(val)
    return -1


array = [2, 1, 5, 2, 3, 3, 4]


print(firstDuplicate(array))
