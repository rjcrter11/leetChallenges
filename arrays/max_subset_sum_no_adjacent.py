'''
Write a function that takes in an array of positive ints and returns the max sum of 
non-adjacent elements in the array.
If the input array is empty, the function should return 0.

array = [75, 105, 120, 75, 90, 135]
output = 330 // 75 + 120 + 135
'''


def maxSubsetSumNoAdjacent(array):
    excl = 0
    incl = 0

    for i in array:
        new_excl = excl if excl > incl else incl

        incl = excl + i
        excl = new_excl

    return excl if excl > incl else incl


array = [75, 105, 120, 75, 90, 135]


print(maxSubsetSumNoAdjacent(array))
