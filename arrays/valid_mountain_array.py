'''
https://leetcode.com/problems/valid-mountain-array/

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

'''

num_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def validMountainArray(arr):
    if len(arr) < 3:
        return False

    peak = arr.index(max(arr))

    if peak == len(arr)-1 or peak == 0:
        return False

    for i in range(0, peak):
        if arr[i] >= arr[i+1]:
            return False
    for i in range(peak+1, len(arr)):
        if arr[i] >= arr[i-1]:
            return False
    return True


print(validMountainArray(num_array))
