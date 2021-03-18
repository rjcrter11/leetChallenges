'''
Given matrix, a rectangular matrix of integers, where each value represents the 
cost of the room, your task is to return the total sum of all rooms that are 
suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

Example

-For

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9.
'''


input = [[0, 1, 1, 2],
         [0, 5, 0, 0],
         [2, 0, 3, 3]]


def matrixElementsSum(matrix):
    row = len(matrix)
    col = len(matrix[0])

    total = 0

    for j in range(col):
        for i in range(row):
            if matrix[i][j] != 0:
                total += matrix[i][j]
            else:
                break
    return total


print(matrixElementsSum(input))
