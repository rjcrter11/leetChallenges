'''
Given an array of positive ints representing coin denominations and a single 
non-negative int n representing a target amount of money, write a function that returns
the smallest number of coins needed to make change for (to sum up to) the target amount
using the given coin denominations.

n = 7
denoms = [1,5,10]

output = 3 // 2x1 + 1x5
'''


def min_coins(n, denoms):
    num_coins = [float('inf') for amount in range(n+1)]
    num_coins[0] = 0

    for denom in denoms:
        for amount in range(len(num_coins)):
            if denom <= amount:
                num_coins[amount] = min(
                    num_coins[amount], num_coins[amount-denom] + 1)
    return num_coins[n] if num_coins[n] != float('inf') else -1


n = 7
denoms = [1, 5, 10]


print(min_coins(n, denoms))
