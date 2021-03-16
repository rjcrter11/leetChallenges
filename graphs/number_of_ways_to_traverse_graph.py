'''
You're given two positive integers representing the width and height of a grid-shaped, rectangular
graph. Write a function that returns the number of ways to reach the bottom right corner of the 
graph when starting at the top left corner. Each move you take must either go down or right.
In other words, you can never move up or left in the graph. 

sample input = 
    width = 4
    height = 3
sample output = 10
'''


def traverseGraph(width, height):
    if width == 1 or height == 1:
        return 1

    return traverseGraph(width-1, height) + traverseGraph(width, height-1)


w = 4
h = 3

print(traverseGraph(w, h))
