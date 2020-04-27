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

        start_timee = datetime.now()  # Общее время
        start_timeShell = time.monotonic()  # ПОИСК
        mobile_number.sort()
        res = InterpolSearch(mobile_number, int(key))
        end_timeShell = time.monotonic()
        timeInterpol = timedelta(seconds=end_timeShell - start_timeShell)

        start_time = datetime.now()  # ПОИСК
        start_timeStd = time.monotonic()
        try:
            resStd = std.index(key)
        except: var = None
        end_timeStd = time.monotonic()
        timeStd = timedelta(seconds=end_timeStd - start_timeStd)

        end_timee = datetime.now()
        alltime = '{}'.format(end_timee - start_timee)

        arr = ', '.join(map(str, mobile_number))
        short = 'true'
        contex = {
            'main_arr': arr,
            'short': short,
            'res': res,
            'place': res + 1,
            'key': str(key),
            'time_interpol': timeInterpol,
            'time_std': timeStd,
            'time_all': alltime,
            'show_all': True,
        }

    return render(request, 'lab2.html', contex)
