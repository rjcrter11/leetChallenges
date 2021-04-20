array = [47, 24, 14, 12, 10, 96, 35]


def bubbleSort(array):
    swap = True

    while swap:
        swap = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swap = True
    return array


print(bubbleSort(array))
