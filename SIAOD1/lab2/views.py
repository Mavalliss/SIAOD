from django.shortcuts import render
from .sort import InterpolSearch
from datetime import timedelta
from datetime import datetime
import time

# Create your views here.

def join(string):
    return ''.join(map(str, string)).replace('][', '\n').replace('[', '').replace(']', '')


def index(request):
    arr = ""
    mainArr = []
    contex = None
    if request.method == "POST":
        mobile_number = request.POST.get('inputarray')
        arr = mobile_number

        std = mobile_number
        key = request.POST.get("inputchar")
        mobile_number = [int(i) for i in mobile_number.split(' ')]

        start_time = datetime.now()  # ПОИСК
        start_timeShell = time.monotonic()
        mobile_number.sort()
        res = InterpolSearch(mobile_number, int(key))
        end_timeShell = time.monotonic()
        timeShell = timedelta(seconds=end_timeShell - start_timeShell)
        print(mobile_number)
        std = mobile_number

        arr = ', '.join(map(str, mobile_number))
        short = 'true'
        contex = {
            'main_arr': arr,
            'short': short,
            'res': res,
            'place': res + 1,
            'key': str(key),
            'time_shell': timeShell,
            'show_all': len(mobile_number) > 23,
        }

    return render(request, 'lab2.html', contex)
