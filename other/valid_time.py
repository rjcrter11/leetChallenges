'''
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.
'''


def validTime(time):
    first = time[0] + time[1]
    second = time[3] + time[4]

    if int(first) > 23 or int(second) > 59:
        return False
    return True


input = "13:58"

print(validTime(input))
