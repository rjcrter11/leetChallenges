'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''


def numSquares(n):

    def is_divided_by(n, count):
        if count == 1:
            return n in square_nums

        for k in square_nums:
            if is_divided_by(n-k, count-1):
                return True
        return False

    square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
    print('Squares', square_nums)

    for count in range(1, n+1):
        if is_divided_by(n, count):
            return count


print(numSquares(12))
