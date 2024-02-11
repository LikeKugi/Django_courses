from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from women.models import Women, Category

# Create your views here.

menu = [{'home': 'Main Page'}, {'about': 'About Us'}, {'add_page': 'Add an Article'}, {'feedback': 'Feedback'},
        {'login': 'Login'}]


def index(request):
    posts = Women.published.all()
    data = {'title': 'Main Page', 'menu': menu, 'posts': posts}
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'About Us', 'menu': menu})


def add_page(request):
    return HttpResponse(f'<h1>Adding Page</h1>')


def feedback(request):
    return HttpResponse(f'<h1>Feedback</h1>')


def login(request):
    return HttpResponse(f'<h1>Login</h1>')


def get_post_by_id(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'women/post.html', context=data)


def categories(request, cat_id: int):
    return HttpResponse(f'<h1>Articles by categories</h1><p>ID: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_slug,
    }

    return render(request, 'women/index.html', context=data)


def archive(request, year):
    return HttpResponse(f'<h1>Archive by years</h1><p>Year: {year}</p>')


def archive_by_month(request, month):
    if 0 < month < 13:
        return HttpResponse(f'<h1>Archive by years</h1><p>Month: {month}</p>')

    return redirect('/')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
