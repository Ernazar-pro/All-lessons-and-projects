from .views import (
    home,
    product_list,
    product_detail,
    about,
    contact,
    create,
)
from django.urls import path

app_name = 'scoop'

urlpatterns = [
    path('',home, name='home'),
    path('sale/',product_list, name='product_list'),
    path('<slug:category_slug>/',product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/',product_detail, name='product_detail'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('create/', create, name='create'),
]