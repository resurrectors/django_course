from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    print(request)
    if month == "january":
        return HttpResponse("Hello, January!")
    elif month == "february":
        return HttpResponse("Hello, February!")
    elif month == "march":
        return HttpResponse("Hello, March!")
    else:
        return HttpResponseNotFound("This is not supported")


def monthly_challenge_by_number(request, month):
    print(request)
    return HttpResponse("The month no is " + str(month))
