'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''


def intersection(nums1, nums2):
    # set_one = set(nums1)
    # set_two = set(nums2)
    # result = []

    # for el in set_one:
    #     if el in set_two:
    #         result.append(el)
    # return result

    # set_one = set(nums1)
    # set_two = set(nums2)

    # return list(set_two & set_one)

    set_one = set(nums1)
    set_two = set(nums2)

    result = [x for x in set_one if x in set_two]
    return result


arr1 = [4, 9, 5]
arr2 = [9, 4, 9, 8, 4]
print(intersection(arr1, arr2))
