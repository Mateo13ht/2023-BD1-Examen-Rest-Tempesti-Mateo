from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns=[
    path('customers/', views.customers),
    path('suppliers/', views.suppliers),
    path('categories/', views.categories),
    path('products/', views.products),
    path('orders/', views.orders),
    path('orderdetails/', views.orderdetails),
    path('employees/', views.employees)
]
