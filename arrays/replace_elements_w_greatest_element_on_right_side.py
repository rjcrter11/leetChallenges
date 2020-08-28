'''
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

'''


def replaceElements(arr):
    # 1
    # max_val = 0
    # result = []

    # for i in range(len(arr)-1, -1, -1):
    #     while arr[i] > max_val:
    #         max_val = arr[i]
    #     result.append(max_val)
    # result.pop()
    # reverse = result[::-1] + [-1]
    # return reverse

    # 2
    # for i in range(0, len(arr)-1):
    #     arr[i] = max(arr[i+1:])
    #     print(arr[i])
    # arr[-1] = -1
    # return arr

    # 3
    max_so_far = arr[-1]
    arr[-1] = -1

    for i in range(len(arr)-2, -1, -1):
        temp = arr[i]
        arr[i] = max_so_far
        max_so_far = max(max_so_far, temp)
    return arr


num_array = [17, 18, 5, 4, 6, 1]

print(replaceElements(num_array))
