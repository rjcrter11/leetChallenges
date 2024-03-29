'''
You're given a 2d array of potentially unequal height and width containing only 0s and 1s.
Each 0 is land, each 1 is part of a river. A river consists of any number of 1s that are
either horizontally or vertically adjacent. The number of adjacent 1s forming a river
determine its size.

sample input = [
    [1,0,0,1,0],
    [1,0,1,0,0],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,1,0]
]

sample output:
[1,2,2,2,5] (numbers don't have to be in this order)

[
    [1, , , 1,  ],
    [1, , 1, ,  ],
    [ , , 1, , 1],
    [1, , 1, , 1],
    [1, , 1, 1, ]
]

'''


def riverSizes(matrix):
    # Write your code here.
    sizes = []

    visited = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]

    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i-1][j]:
        unvisitedNeighbors.append([i-1, j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisitedNeighbors.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        unvisitedNeighbors.append([i, j-1])
    if j < len(matrix[0]) - 1 and not visited[i][j+1]:
        unvisitedNeighbors.append([i, j+1])
    return unvisitedNeighbors


input = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

print(riverSizes(input))
