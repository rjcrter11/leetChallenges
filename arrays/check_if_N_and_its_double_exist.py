'''
https://leetcode.com/problems/check-if-n-and-its-double-exist/

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

'''


def checkIfExist(arr):

    items = set()

    for num in arr:
        print(items)
        if num*2 in items or num/2 in items:
            return True
        else:
            items.add(num)
    return False


num_array = [7, 1, 14, 11]

print(checkIfExist(num_array))
