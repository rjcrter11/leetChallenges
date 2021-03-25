'''
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.
'''


def chessBoardCellColor(cell1, cell2):
    cell1Dark = (ord(cell1[0]) % 2 == 0) != (int(cell1[1]) % 2 == 0)
    cell2Dark = (ord(cell2[0]) % 2 == 0) != (int(cell2[1]) % 2 == 0)

    return cell1Dark == cell2Dark


cell1 = "A1"
cell2 = "C3"


def chessAlt(cell1, cell2):
    letters = list('ABCDEFGH')

    index1 = letters.index(cell1[0])
    index2 = letters.index(cell2[0])

    cell1Dark = (index1 % 2 == 0) != (int(cell1[1]) % 2 == 0)
    cell2Dark = (index2 % 2 == 0) != (int(cell2[1]) % 2 == 0)

    return cell1Dark == cell2Dark


print(chessBoardCellColor(cell1, cell2))
print(chessAlt(cell1, cell2))
