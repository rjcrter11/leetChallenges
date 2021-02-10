'''
Write a function that takes in an array of integers and returns
a boolean representing whether the array is monotonic.
An array is monotonic if its elements, from left to right are
entirely non-increasing or entirely non-decreasing.
array = [-1, -5, -10, -1100, -1101, -1102, -9001]
output = True
'''


def isMonotonic(array):
    up = False
    down = False
    for i in range(1, len(array)):
        if array[i-1] < array[i]:
            up = True
            if down == True:
                return False
        if array[i-1] > array[i]:
            down = True
            if up == True:
                return False
    return True
