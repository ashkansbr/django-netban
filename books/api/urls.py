from django.urls import path
from .views import BookListAPIView, SuggestBooksAPIView

urlpatterns = [
    path('book/list', BookListAPIView.as_view(), name='book-list'),
    path('suggest', SuggestBooksAPIView.as_view(), name='book-suggest'),
]
