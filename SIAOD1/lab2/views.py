from django.shortcuts import render
from .sort import InterpolSearch


# Create your views here.

def join(string):
    return ''.join(map(str, string)).replace('][', '\n').replace('[', '').replace(']', '')


def index(request):
    arr = []
    mainArr = []
    if request.method == "POST":
        mobile_number = request.POST.get('inputarray')
        mobile_number = [int(i) for i in mobile_number.split(' ')]

        mobile_number.sort()
        print(InterpolSearch(mobile_number, 10))

        # print(mobile_number)

        contex = {
            'arr': mobile_number,
        }

    return render(request, 'lab2.html')
