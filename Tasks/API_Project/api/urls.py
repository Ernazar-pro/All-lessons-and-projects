from django.urls import path
from .views import BookAPIView, AuthorAPIView

urlpatterns = [
    path('all/', BookAPIView.as_view(), name='book-list'),
    path('author/', AuthorAPIView.as_view(), name='book-author'),
]