'''
You have deposited a specific amount of money into your bank account.
Each year your balance increases at the same growth rate. With the assumption
that you don't make any additional deposits, find out how long it would
take for your balance to pass a specific threshold.

Example

For deposit = 100, rate = 20, and threshold = 170, the output should be
depositProfit(deposit, rate, threshold) = 3.

Each year the amount of money in your account increases by 20%.
So throughout the years, your balance would be:

year 0: 100;
year 1: 120;
year 2: 144;
year 3: 172.8.
'''


def deposit_profit(deposit, rate, threshold):
    year = 0

    while deposit < threshold:
        deposit += deposit * (rate/100)
        year += 1
    return year


deposit = 100
rate = 20
threshold = 170
print(deposit_profit(deposit, rate, threshold))
