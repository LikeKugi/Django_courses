from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.

menu = ['About Us', 'Add an Article', 'Feedback', 'Login']


def index(request):
    data = {'title': 'Main Page', 'menu': menu}
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'About Us', 'menu': menu})


def categories(request, cat_id: int):
    return HttpResponse(f'<h1>Articles by categories</h1><p>ID: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Articles by slug</h1><p>Slug: {cat_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Archive by years</h1><p>Year: {year}</p>')


def archive_by_month(request, month):
    if 0 < month < 13:
        return HttpResponse(f'<h1>Archive by years</h1><p>Month: {month}</p>')

    return redirect('/')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
