from django.shortcuts import render
from .treatment import Shell, QuickSort


# Create your views here.

def index(request):
    arr = []
    contex = None
    if request.method == "POST":
        mobile_number = request.POST.get('inputarray')

        mobile_number = mobile_number.split('\r\n')
        # print(mobile_number)
        shellsort = []
        quicksort = []
        for i in mobile_number:
            # print(list(map(int, i.replace(" ", ""))))
            shellsort.append(i)
            quicksort.append(i)

        for i in range(0, shellsort.__len__(), 1):
            print(shellsort[i])
            print(list(map(int, shellsort[i].replace(" ", ""))))
            shellsort[i] = Shell(list(map(int, shellsort[i].replace(" ", ""))))
            print(shellsort[i])

        mobile_number = map(int, mobile_number.split())
        for i in mobile_number:
            print(i)
            if i != " ":
                arr.append(i)
            if i == "\r\n":
                arr.append("\n")

        # print(arr)

        # shellsort = arr.copy()
        # quicksort = arr.copy()

        Shell(shellsort)
        QuickSort(quicksort, 0, arr.__len__() - 1)
        time1 = 0
        time2 = 0
        contex = {
            'main_arr': arr,
            'res_arr_shell': shellsort,
            'res_arr_quick': quicksort,
            'time_shell': time1,
            'time_quick': time2,
            'i': {'s', 'q'},
        }

    return render(request, 'mainApp/index.html', contex)
