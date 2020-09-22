'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
'''


def intersect(nums1, nums2):

    hash_map = {}
    result = []

    for x in nums1:
        if x in hash_map:
            hash_map[x] += 1
        else:
            hash_map[x] = 1
    for x in nums2:
        if x in hash_map and hash_map[x] > 0:
            result.append(x)
            hash_map[x] -= 1
    return result


num1 = [4, 9, 5]
num2 = [9, 4, 9, 8, 4]

print(intersect(num1, num2))
