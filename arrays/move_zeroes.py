'''
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

'''


def moveZeroes(nums):

    # zero_array = []
    # result = []

    # for i in nums:
    #     if i == 0:
    #         zero_array.append(i)
    #     else:
    #         result.append(i)
    # final = result + zero_array
    # return final

    if nums == None:
        return None

    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    while write < len(nums):
        nums[write] = 0
        write += 1

    print(nums)


num_arr = [0, 1, 0, 3, 12]
print(moveZeroes(num_arr))
