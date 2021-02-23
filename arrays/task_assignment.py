'''
You're given an integer k representing a number of workers and an array of positive 
integers representing durations of tasks that must be completed by the workers. 
Specifically, each worker must complete two unique tasks and can only work on one
task at a time. The number of tasks will always be equal to 2k such that each worker always 
has exactly two tasks to complete. All tasks are independent of one another and can be completed
in any order. Workers will complete their assigned tasks in parallel, and the time taken
to complete all tasks will be equal to the time taken to complete the longest pair
of tasks.
Write a function that returns the optimal assignment of tasks to each worker such that the 
tasks are completed as fast as possible. Your function should return a list of pairs,
where each pair stores the indices of the tasks that should be completed by one worker.
The pairs should be in the following format: [task1, task2], where the order of task1 and
task2 doesn't matter. 

k = 3
tasks = [1,3,5,3,1,4] 
output = [
    [0,2],
    [4,5],
    [1,3]
]
'''


def taskAssignment(k, tasks):
    pairs = []

    sortedTasks = sorted(tasks)
    mapIndex = mapToIdx(tasks)

    for i in range(k):
        task1 = sortedTasks[i]
        taskI = mapIndex[task1]
        task1Index = taskI.pop()

        task2Sorted = len(sortedTasks) - 1 - i
        task2 = sortedTasks[task2Sorted]
        task2I = mapIndex[task2]
        task2Index = task2I.pop()

        pairs.append([task1Index, task2Index])

    return pairs


def mapToIdx(tasks):
    mapDict = {}

    for i, dur in enumerate(tasks):
        if dur in mapDict:
            mapDict[dur].append(i)
        else:
            mapDict[dur] = [i]

    return mapDict


k = 3
tasks = [1, 3, 5, 3, 1, 4]

print(taskAssignment(k, tasks))
