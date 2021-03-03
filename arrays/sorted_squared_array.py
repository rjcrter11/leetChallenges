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
