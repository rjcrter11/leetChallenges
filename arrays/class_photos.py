'''
It's photo day at the school, and you're the photographer assigned to take class photos.
The class that you'll be photographing has an even number of students, and all these
students are wearing red or blue shirts. You're responsible for arranging the students
in two rows before taking the photo. Each row should contain the same number of students and 
should adhere to the following guidlines:
    - All students wearing red shirts must be in the same row.
    - All students wearing blue shirts must be in the same row.
    - Each student in the back row must be strictly taller than the student directly 
      in front of them in the front row.
You're given 2 input arrays: one containing the heights of all the students with red shirts and another one 
containing the heights of all the students with blue shirts. These arrays will always have the same length,
and eazch height will be a positive integer. Write a function that returns whether or not a class photo
that follows the stated guidelines can be taken.

redShirts = [5,8,1,3,4]
blueShirts = [6,9,2,4,5]

output = True // Place all students with blue shirts in the back row
'''


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    backrow = redShirtHeights if redShirtHeights[0] > blueShirtHeights[0] else blueShirtHeights
    frontrow = redShirtHeights if redShirtHeights[0] < blueShirtHeights[0] else blueShirtHeights

    for i in range(len(backrow)):
        if backrow[i] <= frontrow[i]:
            return False
    return True


redShirts = [5, 8, 1, 3, 4]
blueShirts = [6, 9, 2, 4, 5]

print(classPhotos(redShirts, blueShirts))
