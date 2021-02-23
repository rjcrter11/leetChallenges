'''
Write a function that takes in an array of at least 3 integers and, without sorting the 
input array, returns a sorted array of the 3 largest ints in the input array.
The function should return duplicate ints if necessary; for example, it should return [10,10,12]
for an input array of [10, 5, 9, 10, 12]

array = [141,1,17,-7,-17,-27,18,541,8,7,7]
ouput = [18,141,541]
'''


def findThreeLargestNumbers(arr):

    output = [None] * 3

    first = max(arr)
    output[2] = first
    arr.remove(first)

    second = max(arr)
    output[1] = second
    arr.remove(second)

    third = max(arr)
    output[0] = third

    return output


array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(array))
