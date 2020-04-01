from django.shortcuts import render
from .treatment import Shell, quickSort, join
import time
from datetime import timedelta


# Create your views here.

def index(request):
    arr = []
    mainArr = []
    shellsort = []
    quicksort = []
    contex = None
    if request.method == "POST":
        mobile_number = request.POST.get('inputarray')

        mobile_number = mobile_number.split('\r\n')
        arr = mobile_number

        for i in mobile_number:
            shellsort.append(i)
            quicksort.append(i)
            mainArr.append(i)
        start_time = time.monotonic()
        for i in range(0, shellsort.__len__(), 1):
            mainArr[i] = [int(i) for i in mainArr[i].split(' ')]
        for i in range(0, shellsort.__len__(), 1):
            shellsort[i] = Shell([int(i) for i in shellsort[i].split(' ')])
        for i in range(0, shellsort.__len__(), 1):
            quicksort[i] = quickSort([int(i) for i in quicksort[i].split(' ')])

        end_time = time.monotonic()
        print(timedelta(seconds=end_time - start_time))
        time1 = 0
        time2 = 0
        quicksort = shellsort.copy()

        mainArr = join(mainArr)
        shellsort = join(shellsort)
        quicksort = join(quicksort)

        contex = {
            'main_arr': mainArr,
            'res_arr_shell': shellsort,
            # 'res_arr_shell': strr,
            'res_arr_quick': quicksort,
            'time_shell': time1,
            'time_quick': time2,
            'i': {'s', 'q'},
        }

    # return render(request, 'mainApp/index.html', contex)
    return render(request, 'lab1.html', contex)
