'''
CodeMaster has just returned from shopping. He scanned the check of the items he 
bought and gave the resulting string to Ratiorg to figure out the total number 
of purchased items. Since Ratiorg is a bot he is definitely going to automate it, 
so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear
in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
sumUpNumbers(inputString) = 14.
'''

import re


def sumUpNumbers(input):
    sum1 = 0
    temp1 = re.findall(r'\d+', input)
    if len(temp1) > 0:
        for i in temp1:
            temp = 0
            temp = int(i, 10)
            sum1 = sum1 + temp
    return sum1


inputString = "2 apples, 12 oranges"
print(sumUpNumbers(inputString))
