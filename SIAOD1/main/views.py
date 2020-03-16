from django.shortcuts import render
from .treatment import Shell, QuickSort


# Create your views here.

def index(request):
    arr = []
    shellsort = []
    quicksort = []
    contex = None
    if request.method == "POST":
        mobile_number = request.POST.get('inputarray')

        mobile_number = mobile_number.split('\r\n')
        arr = mobile_number
        # print(mobile_number)

        for i in mobile_number:
            # print(list(map(int, i.replace(" ", ""))))
            shellsort.append(i)
            quicksort.append(i)

        for i in range(0, shellsort.__len__(), 1):
            print(shellsort[i])
            # print(list(map(int, shellsort[i].replace(" ", ""))))
            print([int(i) for i in shellsort[i].split(' ')])
            # print([int(i) for i in QuickSort()])
            shellsort[i] = Shell([int(i) for i in shellsort[i].split(' ')])
            # quicksort[i] = QuickSort([int(i) for i in quicksort[i].split(' ')], 0, quicksort[i].__len__() - 1)
            print(shellsort[i])
        print(shellsort)

        for i in range(1, shellsort.__len__(), 2):
            print(i)
            shellsort.insert(i, '<br>')
        print(shellsort)
        # mobile_number = map(int, mobile_number.split())
        for i in shellsort:
            arr.append(i)
            arr.append('\r\n')
        arr.pop()
        print("arr: " + str(arr))
        #
        # print(arr)

        # shellsort = arr.copy()
        # quicksort = arr.copy()

        # Shell(shellsort)
        # QuickSort(quicksort, 0, arr.__len__() - 1)
        time1 = 0
        time2 = 0
        # arr.append('\n')
        quicksort = shellsort.copy()
        print("shellsort: " + str(shellsort))
        print("quicksort: " + str(quicksort))

        contex = {
            'main_arr': arr,
            'res_arr_shell': shellsort,
            'res_arr_quick': quicksort,
            'time_shell': time1,
            'time_quick': time2,
            'i': {'s', 'q'},
        }

    return render(request, 'mainApp/index.html', contex)
