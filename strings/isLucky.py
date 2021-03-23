'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered 
lucky if the sum of the first half of the digits is equal to the sum of the second half.

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

    pivot = len(s) // 2

    first_half = s[:pivot]
    second_half = s[pivot:len(s)]

    for i in first_half:
        first_sum += int(i)
    for i in second_half:
        second_sum += int(i)

    return first_sum == second_sum


n = 1230
print(isLucky(n))


def luckAlt(n):
    s = str(n)
    pivot = len(s) // 2
    left, right = s[:pivot], s[pivot:len(s)]

    return sum([int(x) for x in left]) == sum([int(x) for x in right])


print(luckAlt(n))
