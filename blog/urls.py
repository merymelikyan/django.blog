from django.urls import path, re_path, register_converter
from . import views

from . import converters

register_converter(converters.FourDigitYearConverter,type_name="year_from_4_numbers")
#register_converter(converters.FourDigitYearConverter, type_name:"year_from_4_numbers")

urlpatterns = [
    path("", views.index),
    path("categories/", views.categories), #http://127.0.0.1:8000/categories/
    path("categories/<int:cat_id>", views.categories_by_id), #http://127.0.0.1:8000/categories/1
    path("categories/<slug:cat_slug>", views.archive),  # http://127.0.0.1:8000/categories/news-about-armenia_12
    path("archive/<year_from_4_numbers:year>/", views.archive)
    #re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),
]