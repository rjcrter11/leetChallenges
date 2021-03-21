'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
'''


def arrayChange(arr):
    target = arr[0] - 1
    steps = 0

    for i in arr:
        if i > target:
            target = i
        else:
            target = target + 1
            steps += target - i

    return steps


array = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]

print(arrayChange(array))
