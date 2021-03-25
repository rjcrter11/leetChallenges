'''
Consider integer numbers from 0 to n - 1 written down along the circle in such a way 
that the distance between any two neighboring numbers is equal 
(note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the 
radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.
'''


def circle_of_numbers(n, firstNumber):
    # return (firstNumber + (n//2)) % n

    halfway = n // 2
    where_first = halfway + firstNumber

    print('mod: 7 % 10 = ', 7 % 10)

    return where_first % n


n = 10
firstNumber = 2

print(circle_of_numbers(n, firstNumber))
