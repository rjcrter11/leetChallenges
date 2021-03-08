'''
Given an array of positive integers representing the values of coins in your possession, write a function that 
returns the minimum amount of change(the min sum of money) that you cannot create. The given coins
can have any positive integer value and aren't necessarily unique.

coins = [5,7,1,1,2,3,22]
output = 20
'''


def non_constructible_change(coins):
    coins.sort()
    current_change = 0

    print(coins)

    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin
    return current_change + 1


coins = [5, 7, 1, 1, 2, 3, 22]


non_constructible_change(coins)
