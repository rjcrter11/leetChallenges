'''
Write a function that takes in two strings and returns the min number of edit operations that need
to be performed on the first string to obtain the second string

input 

str1 = "abc"
str2 = "yabd"

output = 2
'''


def levenshtein(str1, str2):
    size_j = len(str1) + 1
    size_i = len(str2) + 1

    edits = [[x for x in range(size_j)] for y in range(size_i)]

    for i in range(1, size_i):
        edits[i][0] = edits[i-1][0] + 1
    for i in range(1, size_i):
        for j in range(1, size_j):
            if str2[i-1] == str1[j-1]:
                edits[i][j] = edits[i-1][j-1]
            else:
                edits[i][j] = 1 + min(edits[i-1][j-1],
                                      edits[i][j-1], edits[i-1][j])
    return edits[-1][-1]


string1 = 'abc'
string2 = 'yabd'

print(levenshtein(string1, string2))
