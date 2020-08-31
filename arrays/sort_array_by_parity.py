'''
https://leetcode.com/problems/sort-array-by-parity/


Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

'''


def sortArrayByParity(arr):
    i = 0
    j = 0

    while j < len(arr):
        if arr[j] % 2 == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    return arr


nums_array = [3, 1, 2, 4]

print(sortArrayByParity(nums_array))
