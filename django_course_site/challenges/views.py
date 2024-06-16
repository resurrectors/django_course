from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    # month = request.GET.get("month")
    print(request)
    if month == "january":
        return HttpResponse("Hello, January!")
    elif month == "february":
        return HttpResponse("Hello, February!")
    elif month == "march":
        return HttpResponse("Hello, March!")
    else:
        return HttpResponseNotFound("This is not supported")
