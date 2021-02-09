'''
The Fibonacci sequence is defined as followws: the first number of the sequence is 0,
the second number is the sum of the (n-1)th and (n-2)th numbers.
Write a function that takes in an inteher n and return the fib numner
'''


def getNthFib(n):
    # Write your code here.
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)


# with a cache

def getNthFibCache(n, cache=None):
    cache = {1: 0, 2: 1}

    if n in cache:
        return cache[n]
    else:
        cache[n] = getNthFibCache(n-1, cache) + getNthFibCache(n-2, cache)
        return cache[n]
