from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.TwoDigitMonthConverter, 'month')

urlpatterns = [
    path('', views.index),
    path('cat/<int:cat_id>/', views.categories),
    path('cat/<slug:cat_slug>/', views.categories_by_slug),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),
    path('archive/<month:month>/', views.archive_by_month),
    path('about/', views.about),
]