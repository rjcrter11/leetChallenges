'''
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.

'''


def evenDigitsOnly(n):
    nums = str(n)

    for i in nums:
        if int(i) % 2 != 0:
            return False
    return True


n = 248622
print(evenDigitsOnly(n))


def evensAlt(n):
    return all([int(i) % 2 == 0 for i in str(n)])


print(evensAlt(n))
