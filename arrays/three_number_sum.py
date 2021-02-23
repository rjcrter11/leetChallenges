'''
Write a functin that takes in a non-empty array of distinct integers and an integer
representing a target sum. The functin should find all triplets in the array
that sum up to the target sum and return a 2d array of all these triplets.
The numbers in each triplet should be ordered in ascending order, and the triplets 
themselves should be ordered in ascending order with respect to the 
numbers they hold.
If no three numbers sum up to the target sum, the function should return an
empty array.
'''


def threeNumberSum(array, targetSum):
    array.sort()
    output = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            sum = array[i] + array[left] + array[right]
            if sum == targetSum:
                output.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif sum > targetSum:
                right -= 1
            elif sum < targetSum:
                left += 1

    return output
