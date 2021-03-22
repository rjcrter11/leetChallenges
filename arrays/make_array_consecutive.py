'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
each statue having an non-negative integer size. Since he likes to make things 
perfect, he wants to arrange them from smallest to largest so that each statue 
will be bigger than the previous one exactly by 1. He may need some additional 
statues to be able to accomplish that. Help him figure out the minimum number of 
additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.
'''


def makeArrayConsecutive(statues):
    statues.sort()

    count = 0

    for i in range(len(statues)-1):
        current = statues[i]
        next = statues[i+1]

        if current + 1 != next:
            count += (next - current)-1
    return count


statues = [6, 2, 3, 8]
print(makeArrayConsecutive(statues))
