'''
You're given an array of integers where each integer represents a jump of its value in the array.
For instance, the integer 2 represents a jump of two indices forward in the array; the integer
-3 represents a jump of 3 indices backwards in the array.
If a jump spills past the array's bounds, it wraps over to the other side. For instance, 
a jump of -1 at index 0 brings us to the last index in the array.
Write a function that returns a boolean representing whether the jumps in the array form a 
single cycle. A single cycle occurrs if, starting at any index in the array and following
the jumps, every element in the array is visited exactly once before landing back on the 
starting index

sample input: 
array = [2,3,1,-4,-4,2]

sample output:
true 
'''


def hasSingleCycle(arr):
    visited = 0
    currentIdx = 0

    while visited < len(arr):
        if visited > 0 and currentIdx == 0:
            return False
        visited += 1
        currentIdx = getNextIdx(currentIdx, arr)
    return currentIdx == 0


def getNextIdx(currentIdx, arr):
    jump = arr[currentIdx]
    nextIdx = (currentIdx + jump) % len(arr)
    return nextIdx if nextIdx >= 0 else nextIdx + len(arr)


array = [2, 3, 1, -4, -4, 2]
print(hasSingleCycle(array))
