'''
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

'''


def replaceElements(arr):
    max_val = 0
    result = []

    for i in range(len(arr)-1, -1, -1):
        while arr[i] > max_val:
            max_val = arr[i]
        result.append(max_val)
    result.pop()
    reverse = result[::-1] + [-1]
    return reverse


num_array = [17, 18, 5, 4, 6, 1]

print(replaceElements(num_array))
