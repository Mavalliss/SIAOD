def InterpolSearch(A, key):
    __N = len(A)

    x0 = 0
    right = (len(A) - 1)
    while x0 <= right and A[x0] <= key <= A[right]:

        # средняя точка
        mid = x0 + int(((float(right - x0) / (A[right] - A[x0])) * (key - A[x0])))

        # Проверим, мб наше число в середине
        if A[mid] == key:
            return mid

        if A[mid] < key:
            x0 = mid + 1
    return -1


# A = [2, 3, 5, 6, 6, 7, 7, 8, 12, 16, 21, 24, 26, 26, 42, 43, 49, 51, 57, 67, 68, 71, 72, 73, 74, 77, 79, 84, 87]
# print(InterpolSearch(A, 8888))
