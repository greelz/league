from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloWorld(request):
    x = 1
    y = 2
    return HttpResponse("Hello World")
