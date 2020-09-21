'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


def singleNumber(nums):
    hash_map = {}

    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    for el in hash_map:
        if hash_map[el] == 1:
            return el


arr = [4, 1, 2, 1, 2]
print(singleNumber(arr))
