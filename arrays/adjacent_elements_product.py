'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
'''


def adjacentElementsProduct(arr):
    largest = float('-inf')

    for i in range(len(arr)-1):
        product = arr[i] * arr[i+1]

        if product > largest:
            largest = product
    return largest


inputArray = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(inputArray))


def adjacentAlt(arr):
    return max([arr[i] * arr[i+1] for i in range(len(arr)-1)])


print(adjacentAlt(inputArray))
