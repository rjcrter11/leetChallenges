'''
Write a function that takes in a 'special' array and returns its 
products sum. 
A 'special' array is a not-empty array that contains either integers 
or 'special' arrays. The product sum of a 'special' array is the 
sum of its elements, where 'special' arrays inside it are summed themselves
and then multiplied by their level of depth.
The depth of a 'special' array is how far nested it is. For instance, the 
depth of [] ia 1; the depth of the inner array in [[]] is 2; the depth of
the innmost array in [[[]]] is 3. 
Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y,z]]
 is x + 2 * (y+z); the product sum of [x, [y, [z]]] is x + 2(y + 3z)
'''


def productSum(array, multiplier=1):
    sum = 0
    for num in array:
        if type(num) == list:
            sum += productSum(num, multiplier + 1)
        else:
            sum += num
    return sum * multiplier
