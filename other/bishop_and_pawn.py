'''
Given the positions of a white bishop and a black pawn on the standard chess board,
determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move,
but is limited to diagonal movement. Check out the example below to see how it can move:

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.
'''


def bishopAndPawn(bishop, pawn):
    cols = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    if(abs(cols[bishop[0]] - cols[pawn[0]]) == abs(int(bishop[1]) - int(pawn[1]))):
        return True
    return False


bishop = 'h1'
pawn = 'h3'

print(bishopAndPawn(bishop, pawn))
