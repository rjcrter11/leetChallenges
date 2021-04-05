'''
You're given two lists of positive ints: one that contains the speeds of riders wearing red shirts
and one that contains blue. Each rider is represented by a positive int, which is the speed that
they pedal.
Write a function that returns the max possible total speed of all the tandem bicycles
being ridden based on an input parameter, fastest. If fastest = True, your function should
return the max possible total speed; otherwise it should return the min total speed.

sample input:
redShirtSpeeds = [5,5,3,9,2]
blueShirtSpeeds = [3,6,7,2,1]
fastest = True

sample output: 32
'''


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()

    blueShirtSpeeds.sort()
    fasterBlue = blueShirtSpeeds[::-1]

    x = 0
    slowPairs = 0
    fastPairs = 0

    if fastest != True:
        for i in redShirtSpeeds:
            slowPairs += max(i, blueShirtSpeeds[x])
            x += 1
        return slowPairs
    else:
        for i in redShirtSpeeds:
            fastPairs += max(i, fasterBlue[x])
            x += 1
        return fastPairs


redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True


print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))
