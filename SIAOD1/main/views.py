from django.shortcuts import render
from .treatment import Shell, QuickSort
from .models import Data


# Create your views here.

def index(request):
    arr = []
    contex = None
    if request.method == "POST":
        mobile_number = request.POST.get('key')
        # print(mobile_number)
        mobile_number = map(int, mobile_number.split())
        for i in mobile_number:
            if i != " ":
                arr.append(i)
        shellsort = arr.copy()
        quicksort = arr.copy()
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
