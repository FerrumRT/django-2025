from django.contrib import admin
from django.urls import path

from book.views import index, book

urlpatterns = [
    path('', index, name='index'),
    path('<int:book_id>/', book, name='book'),
]
