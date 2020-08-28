'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

'''


def removeDuplicates(nums):

    x = 0

    if len(nums) < 2:
        return len(nums)

    for i in range(len(nums)):
        print("array val: ", nums[i])
        print("x out: ", nums[x])
        if nums[x] != nums[i]:
            print("val in loop: ", nums[i])
            print("X: ", nums[x])
            x += 1
            nums[x] = nums[i]
    return x


nums_arr = [1, 1, 2, 3, 4, 4]
print(removeDuplicates(nums_arr))
print(nums_arr)
