from django.urls import path

from api import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>', views.product_detail, name='product_detail'),
]