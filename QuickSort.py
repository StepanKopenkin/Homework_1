def quickSort(alist, index, reverse):
    if reverse == True:
        quickSortHelper_reversed(alist, index, 0, len(alist[1]) - 1)
    else:
        quickSortHelper(alist, index, 0, len(alist[1]) - 1)


def quickSortHelper(alist, index, first, last):
    if first < last:
        splitpoint = partition(alist, index, first, last)

        quickSortHelper(alist, index, first, splitpoint - 1)
        quickSortHelper(alist, index, splitpoint + 1, last)


def quickSortHelper_reversed(alist, index, first, last):
    if first < last:
        splitpoint = partition_reversed(alist, index, first, last)

        quickSortHelper_reversed(alist, index, first, splitpoint - 1)
        quickSortHelper_reversed(alist, index, splitpoint + 1, last)


def partition(alist, index, first, last):
    pivotvalue = alist[index][first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[1][leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[index][rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            for x in range(len(alist)):
                temp = alist[x][leftmark]
                alist[x][leftmark] = alist[x][rightmark]
                alist[x][rightmark] = temp

    for x in range(len(alist)):
        temp = alist[x][first]
        alist[x][first] = alist[x][rightmark]
        alist[x][rightmark] = temp

    return rightmark


def partition_reversed(alist, index, first, last):
    pivotvalue = alist[index][first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[1][leftmark] >= pivotvalue:
            leftmark = leftmark + 1

        while alist[index][rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            for x in range(len(alist)):
                temp = alist[x][leftmark]
                alist[x][leftmark] = alist[x][rightmark]
                alist[x][rightmark] = temp

    for x in range(len(alist)):
        temp = alist[x][first]
        alist[x][first] = alist[x][rightmark]
        alist[x][rightmark] = temp

    return rightmark
