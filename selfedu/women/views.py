from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Women application page')


def categories(request):
    return HttpResponse('<h1>Articles by categories</h1>')