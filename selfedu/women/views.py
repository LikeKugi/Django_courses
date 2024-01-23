from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('Women application page')


def categories(request, cat_id: int):
    return HttpResponse(f'<h1>Articles by categories</h1><p>ID: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Articles by slug</h1><p>Slug: {cat_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Archive by years</h1><p>Year: {year}</p>')


def archive_by_month(request, month):
    return HttpResponse(f'<h1>Archive by years</h1><p>Month: {month}</p>')
