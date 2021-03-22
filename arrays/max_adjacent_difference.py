'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.


'''


def max_adjacent_diff(a):
    max_dif = -1000

    for i in range(len(a)-1):
        sub = abs(a[i]-a[i+1])
        if sub > max_dif:
            max_dif = sub
    return max_dif


input = [-1, 4, 10, 3, -2]
print(max_adjacent_diff(input))


def max_diff_alt(a):
    return max(abs(a[i]-a[i+1]) for i in range(len(a)-1))


print(max_diff_alt(input))
