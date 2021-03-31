'''Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52
For n = 1001, the output should be
deleteDigit(n) = 101.
'''


def delete_digit(n):
    n = str(n)
    res = 0

    for i in range(len(n)):
        res = max(res, int(n[:i] + n[i+1:]))
    return res


n = 152
print(delete_digit(n))
