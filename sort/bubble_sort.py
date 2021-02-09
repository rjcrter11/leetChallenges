'''
Write a function that takes in an array and returns a sorted version of that array.
Use the bubble sort algorithm to sort the array.

array = [8,5,2,9,5,6,3]
output = [2,3,5,5,6,8,9]
'''


def bubbleSort(array):
    hasSwapped = True
    count = 0

    while hasSwapped:
        hasSwapped = False

        for i in range(len(array) - count - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                hasSwapped = True
        count += 1
    return array


arr = [8, 5, 2, 9, 5, 6, 3]

result = bubbleSort(arr)

print(result)
