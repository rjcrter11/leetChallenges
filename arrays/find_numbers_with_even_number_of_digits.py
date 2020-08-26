'''


Given an array nums of integers, return how many of them contain an even number of digits.
 
Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
'''


def findNumbers(nums):
    result = []
    count = 0
    for x in nums:
        x = len(str(x))
        print(x)
        result.append(int(x))
    print(result)

    result = [result.count(i) for i in result if i % 2 == 0]
    print(result)

    for i in result:
        count += 1

    return count


input_nums = [12, 345, 2, 6, 7896]

print(findNumbers(input_nums))
