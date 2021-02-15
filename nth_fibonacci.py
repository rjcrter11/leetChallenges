'''
The fibonacci sequence is defined as follows: the first number of the sequence is 0, the 
second number is 1, and the nth number is the sum of the (n-1)th and (n-2)th numbers.
Write a function that takes in an integer n and returns the nth Fibonacci number.
'''


def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)


print(getNthFib(8))


def getNthFibWithCache(n, cache=None):
    cache = {1: 0, 2: 1}

    if n in cache:
        return cache[n]
    else:
        cache[n] = getNthFibWithCache(
            n-1, cache) + getNthFibWithCache(n-2, cache)
        return cache[n]


print('Cached: ', getNthFibWithCache(8))
