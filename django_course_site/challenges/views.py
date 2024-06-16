from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    print(request)
    return HttpResponse("This is working")


def february(request):
    print(request)
    return HttpResponse("This is february")
