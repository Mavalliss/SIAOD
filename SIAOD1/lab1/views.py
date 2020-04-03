from django.shortcuts import render
from .treatment import Shell, quickSort, join
import time
from datetime import timedelta
from datetime import datetime
import random


# Create your views here.

def index(request):
    arr = []
    mainArr = []
    shellsort = []
    quicksort = []
    contex = None
    if request.method == "POST":
        mobile_number = request.POST.get('inputarray')
        onlyTime = request.POST.get('checkbox')

        mobile_number = mobile_number.split('\r\n')
        arr = mobile_number

        for i in mobile_number:
            shellsort.append(i)
            quicksort.append(i)
            mainArr.append(i)

        for i in range(0, shellsort.__len__(), 1):
            mainArr[i] = [int(i) for i in mainArr[i].split(' ')]

        start_timee = datetime.now()  # сортировка Шелла
        start_timeShell = time.monotonic()
        for i in range(0, shellsort.__len__(), 1):
            shellsort[i] = Shell([int(i) for i in shellsort[i].split(' ')])
        end_timeShell = time.monotonic()
        timeShell = timedelta(seconds=end_timeShell - start_timeShell)

        start_timeQuick = time.monotonic()  # быстрая сортировка
        for i in range(0, shellsort.__len__(), 1):
            quicksort[i] = quickSort([int(i) for i in quicksort[i].split(' ')])
        end_timeQuick = time.monotonic()
        timeQuick = timedelta(seconds=end_timeQuick - start_timeQuick)

        end_timee = datetime.now()
        print('Duration: {}'.format(end_timee - start_timee))
        alltime = '{}'.format(end_timee - start_timee)

        quicksort = shellsort.copy()
        sortArr = mainArr.copy()

        start_time = time.monotonic()  # встроенная соритровка
        sortArr.sort()
        end_time = time.monotonic()
        timeSort = timedelta(seconds=end_time - start_time)

        sortArr = join(sortArr)
        mainArr = join(mainArr)
        shellsort = join(shellsort)
        quicksort = join(quicksort)

        contex = {
            'main_arr': mainArr,
            'res_arr_shell': shellsort,
            'res_arr_quick': quicksort,
            'res_arr_sort': sortArr,
            'time_shell': timeShell,
            'time_quick': timeQuick,
            'time_sort': timeSort,
            'time_all': alltime,
            'i': {'s', 'q', 'd'},
            'only_time': onlyTime,
        }

    # return render(request, 'mainApp/index.html', contex)
    return render(request, 'lab1.html', contex)
