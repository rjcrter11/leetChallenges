'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''


def sortByHeight(arr):
    heights = [x for x in arr if x != -1]
    heights.sort()
    print(heights)

    for x in range(len(arr)):
        arr[x] = heights.pop(0) if arr[x] != -1 else arr[x]

    return arr


a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))
