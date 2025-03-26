from django.urls import path

from api import views

urlpatterns = [
    path('products/', views.product_list, name='product_list_api'),
    path('products/<int:pk>', views.product_detail, name='product_detail_api'),
    path('categories/', views.category_list, name='category_list_api'),
    path('categories/<int:pk>', views.category_detail, name='category_detail_api'),
]