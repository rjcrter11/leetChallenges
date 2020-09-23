'''
Determine if a 9x9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
'''


def isValidSoduku(board):
    def has_repitition(ls):
        stats = dict()
        for i in ls:
            if i != '.':
                stats[i] = stats.get(i, 0) + 1
        for val in stats.values():
            if val > 1:
                return True
        return False

    for line in board:
        if has_repitition(line):
            return False

    for line in zip(*board):
        if has_repitition(line):
            return False

    sub_boxes = []

    for x_step in range(0, 3):
        for y_step in range(0, 3):
            sub_box = []
            for i in range(0, 3):
                for j in range(0, 3):
                    sub_box.append(board[i+x_step*3][j+y_step*3])
            sub_boxes.append(sub_box)

    for sub_box in sub_boxes:
        if has_repitition(sub_box):
            return False
    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(isValidSoduku(board))
