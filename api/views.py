from django.shortcuts import render

from rest_framework.response import Response
from api.serializers import *
from api.models import *
from rest_framework.decorators import api_view
from rest_framework import status

#customers
@api_view(['GET', 'POST'])
def customers(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def customer(request, customerid):
    try:
        customer = Customers.objects.get(customerid=customerid)
    except customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = CustomersSerializer(customer, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomersSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_200_OK)

#supplier 
@api_view(['GET', 'POST'])
def suppliers(request):
    if request.method == 'GET':
        suppliers = Suppliers.objects.all()
        serializer = SuppliersSerializer(suppliers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuppliersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def supplier(request, supplierid):
    try:
        supplier = Suppliers.objects.get(supplierid=supplierid)
    except supplier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = SuppliersSerializer(supplier, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuppliersSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_200_OK)
    
#categories
@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def categorie(request, categoryid):
    try:
        categorie = Categories.objects.get(categoryid=categoryid)
    except categorie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = CategoriesSerializer(categorie, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriesSerializer(categorie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categorie.delete()
        return Response(status=status.HTTP_200_OK)

#products
@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product(request, productid):
    try:
        product = Products.objects.get(productid=productid)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = ProductsSerializer(product, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_200_OK)
    
#orders 
@api_view(['GET', 'POST'])
def orders(request):
    if request.method == 'GET':
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order(request, orderid):
    try:
        order = Orders.objects.get(orderid=orderid)
    except order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = OrdersSerializer(order, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrdersSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_200_OK)
    
#Orderdetails 
@api_view(['GET', 'POST'])
def orderdetails(request):
    if request.method == 'GET':
        orderdetails = Orderdetails.objects.all()
        serializer = OrderdetailsSerializer(orderdetails, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderdetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def orderdetail(request, orderid):
    try:
        orderdetail = Orderdetails.objects.get(orderid=orderid)
    except orderdetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = OrderdetailsSerializer(orderdetail, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderdetailsSerializer(orderdetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        orderdetail.delete()
        return Response(status=status.HTTP_200_OK)  
    
#employees 
@api_view(['GET', 'POST'])
def employees(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee(request, employeeid):
    try:
        employee = Employees.objects.get(employeeid=employeeid)
    except employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = EmployeesSerializer(employee, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeesSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_200_OK) 

 
@api_view(['GET'])
def fechaDespuesDe(request):
    orders = Orders.objects.filter(orderdate__gt="1996-12-24")
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fechaAntesDE(request):
    orders = Orders.objects.filter(orderdate__lt="1996-12-24")
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def RangoFecha(request):
    orders = Orders.objects.filter(orderdate__range=("1996-12-24","1997-1-1"))
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def empiezaPor(request):
    customers = Customers.objects.filter(contactname__startswith="E")
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def terminaEn(request):
    customers = Customers.objects.filter(contactname__endswith="e")
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)


#parte de la actividad 1
@api_view(['GET'])
def ordenado(request):
    employees = Employees.objects.all().order_by('salary')
    serializer = EmployeesSerializer(employees, many=True)
    return Response(serializer.data)


#parte de la actividad 2
@api_view(['GET'])
def poridcategori(request):
    products = Products.objects.all().order_by('categoryid')
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ordenadoAlReves(request):
    customers = Customers.objects.all().order_by('-contactname')
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)