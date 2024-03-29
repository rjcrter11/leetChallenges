'''
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
'''


def extractEachKth(input, k):
    return [num for (idx, num) in enumerate(input) if (idx+1) % k != 0]


inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(extractEachKth(inputArray, 3))
