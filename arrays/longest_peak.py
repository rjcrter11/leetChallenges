'''
Write a function that takes in an array of integers and returns
the length of the longest peak in the array.
A peak is defined as adjacent integers in the array that are strictly
increasing until they reach a tip(the highest value in the peak), at which point
they become strictly decreasing. At least 3 int are required to form a peak. 

array=[1,2,3,3,4,0,10,6,5,-1,-3,2,3]
ouput = 6 // 0, 10, 6, 5, -1, -3
'''


def longestPeak(arr):
    i = 0
    count = 0

    while i < len(arr)-1:
        base = i
        while i+1 < len(arr) and arr[i] < arr[i+1]:
            i += 1
        if base == i:
            i += 1
            continue
        peak = i

        while i+1 < len(arr) and arr[i] > arr[i+1]:
            i += 1

        if peak == i:
            i += 1
            continue
        count = max(count, i-base+1)
    return count


peakArr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

print(longestPeak(peakArr))
