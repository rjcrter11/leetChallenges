'''
Write a function that takes in a non-empty array of integers and returns the maximum sum that 
can be obtained by summing up all of the integers in a non-empty subarray of the input array.
A subarray must only contain adjacent numbers(numbers next to each other in the input array).

sample input: 
array = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]

sample output:
19 // [1,3,-2,3,4,7,2,-9,6,3,1]
'''


def kadanealgo(arr):

    for i in range(1, len(arr)):
        if arr[i-1] > 0:
            arr[i] += arr[i-1]
    return max(arr)


array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanealgo(array))
