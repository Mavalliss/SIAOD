from datetime import datetime


def Shell(seq):
    start_time = datetime.now()
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

    return seq


def Partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def QuickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = Partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)


data = [22, 7, 2, -5, 8, 4]
Shell(data)
# print data  # [-5, 2, 4, 7, 8, 22]
