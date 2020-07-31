'''
https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''


def search(nums, target):
    n = len(nums)

    pivot = find_pivot(nums, 0, n-1)

    if pivot == -1:
        return binary_search(nums, 0, n-1, target)
    if nums[pivot] == target:
        return pivot
    if nums[0] <= target:

        return binary_search(nums, 0, pivot-1, target)
    return binary_search(nums, pivot+1, n-1, target)


def find_pivot(nums, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = (low + high) // 2

    if nums[mid] > nums[mid + 1]:
        return mid
    if nums[mid] < nums[mid - 1]:
        print("Check")
        return -1
    if nums[low] >= nums[mid]:
        return find_pivot(nums, low, mid-1)
    return find_pivot(nums, mid+1, high)


def binary_search(nums, low, high, target):
    if high < low:
        return -1
    mid = (low + high) // 2
    if target == nums[mid]:
        return mid
    if target >= nums[mid]:
        return binary_search(nums, (mid + 1), high, target)
    return binary_search(nums, low, (mid - 1), target)


input_arr = [6, 7, 1, 2, 3, 4, 5]
target = 1

print(search(input_arr, target))
