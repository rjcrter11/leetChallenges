'''
Your task is to make a function that can take any non-negative integer as an argument 
and return it with its digits in descending order. Essentially, 
rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
'''

from typing import Tuple


def descending_order(num):
    listed = list(str(num))
    listed.sort(reverse=True)

    return int("".join(listed))


nums = 42145


print(descending_order(nums))
