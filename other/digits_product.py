'''
Given an integer product, find the smallest positive (i.e. greater than 0) 
integer the product of whose digits is equal to product. 
If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
'''


def digitsProduct(product):
    if product == 0:
        return 10

    for i in range(3600):
        a = 1
        for j in str(i):
            a *= int(j)
        if a == product:
            return i
    return -1


product = 12
print(digitsProduct(product))
