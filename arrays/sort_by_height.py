'''
Some people are standing in a row in a park. There are trees between them 
which cannot be moved. Your task is to rearrange the people by their heights 
in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]
'''

arr = [-1, 150, 190, 170, -1, -1, 160, 180]


def sortByHeight(a):
    heights = [n for n in a if n != -1]

    heights.sort()

    for i in range(len(a)):
        a[i] = heights.pop(0) if a[i] != -1 else a[i]
    return a


print(sortByHeight(arr))
