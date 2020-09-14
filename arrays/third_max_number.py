'''
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


def third_max(nums):
    num_set = set(nums)
    max_num = max(num_set)

    if len(num_set) < 3:
        return max_num

    num_set.remove(max_num)
    new_max = max(num_set)
    num_set.remove(new_max)
    return max(num_set)


arr = [3, 2, 1]
print(third_max(arr))
