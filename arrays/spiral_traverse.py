'''
Write a function that takes in an n x m two-d array(that can be square-shaped when n == m)
and returns a 1d array of all the array's elements in a sprial order. 
Spiral order starts at the top left corner of the 2d array, goes to the right, and 
proceeds in a spiral pattern all the way until every element has been visited.

array = [
    [1,  2, 3,4],
    [12,13,14,5],
    [11,16,15,6],
    [10, 9, 8,7]
]
output = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
'''


def spiralTraverse(array):
    output = []
    traverseHelper(array, 0, len(array)-1, 0, len(array[0])-1, output)
    return output


def traverseHelper(array, startRow, endRow, startCol, endCol, output):
    if startRow > endRow or startCol > endCol:
        return

    for col in range(startCol, endCol + 1):
        output.append(array[startRow][col])

    for row in range(startRow+1, endRow+1):
        output.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):
        if startRow == endRow:
            break
        output.append(array[endRow][col])

    for row in reversed(range(startRow+1, endRow)):
        if startCol == endCol:
            break
        output.append(array[row][startCol])
    traverseHelper(array, startRow+1, endRow-1, startCol+1, endCol-1, output)


arr = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

result = spiralTraverse(arr)
print(result)
