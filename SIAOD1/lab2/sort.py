# интерполяционный поиск
def InterpolSearch(A, key):
    __N = len(A)

    mid = 0
    left = 0
    right = __N - 1
    while A[left] <= key <= A[right]:
        mid = left + ((key - A[left]) * (right - left)) / A[right] - A[left]
        mid = int(mid)
        if A[mid] < key:
            left = mid + 1
        elif A[mid] > key:
            right = mid - 1
        else:
            return mid

        if A[left] == key:
            return left
        else:
            return -1


# i = 0
# A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
# key = int(input("Искомый элемент: "))
# print("Исходный массив: ", end='')
# for i in range(0, 17):
#     print(str(A[i]) + ' ', end='')
# if InterpolSearch(key) == -1:
#     print("\nЭлемент не найден")
# else:
#     print("\nНомер элемента: " + str(int(InterpolSearch(key)) + 1))

# print(InterpolSearch(A, 2))
