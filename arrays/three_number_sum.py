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
