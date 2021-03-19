'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
'''


def isLucky(n):
    s = str(n)

    first_sum = 0
    second_sum = 0

    mid = len(s)//2
    fist_half = s[0:mid]
    second_half = s[mid:len(s)]

    for x in fist_half:
        first_sum += int(x)
    for x in second_half:
        second_sum += int(x)
    return first_sum == second_sum


num = 1230

print(isLucky(num))
