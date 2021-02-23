'''
Given an array of distinct positive integers representing coin denominations and 
a single non-negative integer n represents a target amount of money, write a function that 
returns the number of ways to make change for that target using the given coin denominations

'''


def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ways = [0 for amount in range(n+1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount-denom]
                print(ways)
    return ways[n]


num = 10
denoms = [1, 5, 10, 25]

print(numberOfWaysToMakeChange(num, denoms))
