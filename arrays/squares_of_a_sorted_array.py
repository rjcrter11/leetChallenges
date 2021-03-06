'''
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

'''


def sortedSquares(nums):
    # 1
    # result = []

    # for x in nums:
    #     x *= x
    #     result.append(x)

    # 2
    # return sorted(result)

    # for x in range(len(nums)):
    #     nums[x] *= nums[x]

    # return sorted(nums)

    # 3
    return sorted([x*x for x in nums])


nums_array = [-4, -1, 0, 3, 10]

print(sortedSquares(nums_array))
