'''
Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping
intervals, and returns the new intervals in no particular order.

sample input:
intervals = [[1,2],[3,5],[4,7],[6,8],[9,10]]

sample output:
[[1,2], [3,8], [9,10]]
'''


def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sortedIntervals = sorted(intervals, key=lambda x: x[0])

    mergedIntervals = []
    current = sortedIntervals[0]
    mergedIntervals.append(current)

    for next in sortedIntervals:
        _, currentEnd = current
        nextStart, nextEnd = next

        if currentEnd >= nextStart:
            current[1] = max(currentEnd, nextEnd)
        else:
            current = next
            mergedIntervals.append(current)
    return mergedIntervals


intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
print(mergeOverlappingIntervals(intervals))
