'''
Write a function that takes in an array of integers and returns a sorted version of 
that array. Use the insertion sort algorithm
'''


def insertionSort(array):

    for i in range(len(array)):
        current = array[i]

        while i > 0 and current < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array


arr = [8, 5, 2, 9, 5, 6, 3]

insert = insertionSort(arr)
print(insert)
