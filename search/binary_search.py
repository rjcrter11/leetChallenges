'''
Write a function that takes in a sorted array of integers as well as
a target integer. The function should use the Binary Search algorithm to 
determine if the target integer is contained in the array and should return 
its index if it is, otherwise -1
'''


def binarySearch(array, target):
    return searchHelper(array, target, 0, len(array)-1)


def searchHelper(array, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return searchHelper(array, target, low, mid-1)
    else:
        return searchHelper(array, target, mid+1, high)


array = [1, 5, 23, 111]
target = 5

print(binarySearch(array, target))
