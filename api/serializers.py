from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'        

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'           

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'      

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'   

class OrderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetails
        fields = '__all__'           

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'    