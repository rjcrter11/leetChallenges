'''
You're given a 2d array of potentially unequal height and width containing only 0s and 1s.
The matrix represents a two-toned image, where each 1 represents black and each 0
represents white. An island is defined as any number of 1s that are horizontally or
verticallly adjacent(but not diagonally) and that don't touch the border of the image.
Write a function that returns a modified version of the input matrix, where all of the islands
are removed. You remove an island by replacing it with 0s

sample matrix =
[
    [1,0,0,0,0,0],
    [0,1,0,1,1,1],
    [0,0,1,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,1,0,0],
    [1,0,0,0,0,1]
]

sample output =
[
    [1,0,0,0,0,0],
    [0,0,0,1,1,1],
    [0,0,0,0,1,0],
    [1,1,0,0,1,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,1]
]
'''


def removeIslands(matrix):
    # Write your code here.
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix)-1
            colIsBorder = col == 0 or col == len(matrix[row])-1
            isBorder = rowIsBorder or colIsBorder
            if not isBorder:
                continue

            if matrix[row][col] != 1:
                continue

            changeOnesConnectedToBorderToTwos(matrix, row, col)

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                color = matrix[row][col]
                if color == 1:
                    matrix[row][col] = 0
                elif color == 2:
                    matrix[row][col] = 1
        return matrix


def changeOnesConnectedToBorderToTwos(matrix, startRow, startCol):
    stack = [(startRow, startCol)]

    while len(stack) > 0:
        currentPosition = stack.pop()
        currentRow, currentCol = currentPosition

        matrix[currentRow][currentCol] = 2

        neighbors = getNeighbors(matrix, currentRow, currentCol)

        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue

            stack.append(neighbor)


def getNeighbors(matrix, row, col):
    neighbors = []

    numRows = len(matrix)
    numCols = len(matrix[row])

    if row-1 >= 0:
        neighbors.append((row-1, col))
    if row+1 < numRows:
        neighbors.append((row+1, col))
    if col-1 >= 0:
        neighbors.append((row, col-1))
    if col+1 < numCols:
        neighbors.append((row, col+1))

    return neighbors


islands = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

print(removeIslands(islands))
