'''
https://leetcode.com/problems/max-consecutive-ones/

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

'''


def findMaxConsecutiveOnes(nums):
    count = 0
    max_ones = 0

    for x in nums:
        if x == 1:
            count += 1
        else:
            max_ones = max(max_ones, count)
            count = 0

    return max(max_ones, count)


number_arr = [1, 1, 0, 1, 1, 1]

print(findMaxConsecutiveOnes(number_arr))
