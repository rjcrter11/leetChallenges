'''
Write a function that takes two non-empty arrays of
integers, finds the pair of numbers(one from each array)
whose absolute difference is closest to zero, and returns
an array containing these two numbers, with the number from
the first array in the first position

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

output [28, 26]
'''


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()


arrayTwo.sort()

smallest = float('inf')
i = 0
j = 0

while i < len(arrayOne) and j < len(arrayTwo):
		value = abs(arrayOne[i] - arrayTwo[j])
		if value == 0:
			return [arrayOne[i], arrayTwo[j]]
		if value < smallest:
			smallest = value
			print(smallest)
			output = [arrayOne[i], arrayTwo[j]]
		if arrayOne[i] < arrayTwo[j]:
			i += 1
		else:
			j += 1
	return output
