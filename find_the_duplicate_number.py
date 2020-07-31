'''
https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
'''


def find_duplicate(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return num
        num_set.add(num)


num_array = [1, 3, 4, 2, 2]

print(find_duplicate(num_array))
