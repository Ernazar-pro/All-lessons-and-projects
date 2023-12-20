from django.urls import path
from .views import ProductAPIView, ProductDetailAPIView

urlpatterns = [
    path('products', ProductAPIView.as_view(), name='products-list'),
    path('api/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]