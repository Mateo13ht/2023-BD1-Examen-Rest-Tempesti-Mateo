from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns=[
    #customers
    path('customers/', views.customers),
    path('customers/<str:customerid>/', views.customer),

    #suppliers
    path('suppliers/', views.suppliers),
    path('suppliers/<int:supplierid>/', views.supplier),

    #categories
    path('categories/', views.categories),
    path('categories/<int:categoryid>/', views.categorie),

    #products
    path('products/', views.products),
    path('products/<int:productid>/', views.product),

    #orders
    path('orders/', views.order),
    path('orders/<int:orderid>/', views.order),

    #orderdetails
    path('orderdetails/', views.orderdetails),
    path('orderdetails/<int:orderid>/', views.orderdetail),

    #employees 
    path('employees/', views.employees),
    path('employees/<int:employeeid>/', views.employee),

    #Pruebas
    path('fechadespuesde/', views.fechaDespuesDe),
    path('fechaantesde/', views.fechaAntesDE),
    path('rangofecha/', views.RangoFecha),
    path('empiezapor/', views.empiezaPor),
    path('terminaen/', views.terminaEn),
    path('ordenado/', views.ordenado),
    path('poridcategori/', views.poridcategori),
    path('ordenadoalreves/', views.ordenadoAlReves)
]
