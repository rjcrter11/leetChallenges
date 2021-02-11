'''
Given 2 non-empty arrays of integers, write a function that determines whether the second
array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array, 
but that are in the same order as the appear in the array. For instance, the numbers [1,3,4] 
form a subsequence of the array and the array itself are both valid subsequences of the array

array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

output = true
'''


def isValidSubsequence(array, sequence):
    seqIdx = 0

    for num in array:
        if seqIdx == len(sequence):
            break
        if num == sequence[seqIdx]:
            seqIdx += 1
    return seqIdx == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


print(isValidSubsequence(array, sequence))
