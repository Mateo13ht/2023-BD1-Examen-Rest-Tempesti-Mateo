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

class EmployeesSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'    

class ShippersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shippers
        fields = '__all__'  

class EmployeesSerializer(serializers.ModelSerializer):
    reportsto = EmployeesSerializer2(many=False)
    class Meta:
        model = Employees
        fields = '__all__'  

class OrdersSerializer(serializers.ModelSerializer):
    customerid = CustomersSerializer(many=False)
    employeeid = EmployeesSerializer(many=False)
    shipvia = ShippersSerializer(many=False)

    class Meta:
        model = Orders
        fields = '__all__'     

class ProductsSerializer(serializers.ModelSerializer):
    supplierid = SuppliersSerializer(many=False)
    categoryid = CategoriesSerializer(many=False)
    
    def create(self, validated_data):
        supplier_data = validated_data.pop('supplierid', None)
        category_data = validated_data.pop('categoryid', None)

        product = Products.objects.create(**validated_data)

        if supplier_data:
            supplier = Suppliers.objects.get_or_create(**supplier_data)
            product.supplierid = supplier[0]

        if category_data:
            category = Categories.objects.get_or_create(**category_data)
            product.categoryid = category[0]

        product.save()
        return product
    
    class Meta:
        model = Products
        fields = '__all__'  

class OrderdetailsSerializer(serializers.ModelSerializer):
    productid = ProductsSerializer(many=False)
    class Meta:
        model = Orderdetails
        fields = '__all__'    