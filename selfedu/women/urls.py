from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.TwoDigitMonthConverter, 'month')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.add_page, name='add_page'),
    path('feedback/', views.feedback, name='feedback'),
    path('login', views.login, name='login'),
    path('post/<slug:post_slug>', views.get_post_by_id, name='post'),
    path('cat/<slug:cat_slug>/', views.categories_by_slug, name='category'),
]
