'''
Write a function that takes in a non-empty array of integers and returns an array
of the same length, where each element in the output array is equal to the product of
every other number in the input array.
In other words, the value at output[i] == the product of every number in the 
input array other than input[i].
array = [5,1,4,2]
output = [8,40,10,20]
'''


def arrayOfProducts(arr):
    output = []

    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product *= arr[j]
        output.append(product)
    return output


array = [5, 1, 4, 2]

print(arrayOfProducts(array))
