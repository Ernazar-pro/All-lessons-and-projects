from django.urls import path
'''from .views import  CafeAPIView, CafeDetailAPIView, MenuAPIView, MenuDetailAPIView, FoodAPIView, FoodDetailAPIView'''
from .views import MenuAPI, MenuDetailAPI

urlpatterns = [
    path('menu/', MenuAPI.as_view()),
    path('menu/<int:pk>/', MenuDetailAPI.as_view())
]
