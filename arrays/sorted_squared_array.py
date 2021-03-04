'''
Write a function that takes in a non-empty array of integers that are sorted in ascending order and 
returns a new array of the same length with the squares of the original integers also sorted in ascending
order 

array = [1,2,3,5,6,8,9]
output = [1,4,9,25,36,64,81]
'''


def sorted_squared_array(arr):
    output = []

    for num in arr:
        squared = num * num
        output.append(squared)
    return sorted(output)


array = [1, 2, 3, 5, 6, 8, 9]

print(sorted_squared_array(array))


def sorted_squared_alt(arr):

    sorted_squares = [0 for _ in arr]
    smallIdx = 0
    largeIdx = len(arr)-1

    for idx in reversed(range(len(arr))):
        smallVal = arr[smallIdx]
        largeVal = arr[largeIdx]

        if abs(smallVal) > abs(largeVal):
            sorted_squares[idx] = smallVal * smallVal
            smallIdx += 1
        else:
            sorted_squares[idx] = largeVal * largeVal
            largeIdx -= 1
    return sorted_squares


array2 = [-10, -5, 0, 5, 10]

print(sorted_squared_alt(array2))
