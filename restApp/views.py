from django.shortcuts import render, redirect
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from .serializer import MySerializer

from bmpapp.models import Profile, Product
# Create your views here.


@api_view(['GET'])
def enpoints(request):
    data = {
        'Overview': '/overview',
        'Create User' : '/create',
        'Update User' : '/update',
        'Delete User' : '/delete',
    }
    return Response(data)


# ================================ GET =============================
@api_view(['GET'])
def overview(request):

    if request.method == 'GET':
        product = Product.objects.all()
        myserializer = MySerializer(product, many=True)

    return Response(myserializer.data)


@api_view(['POST'])
def create(request):
        
    product = Product.objects.create(
    name = request.data['name'],
    price = request.data['price'],
    description = request.data['description'],
    image = request.data['image']
    )
        
    serializer = MySerializer(product, many =False)
    return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    product = Product.objects.get(id = pk)

    if request.method == 'GET':
        serializer = MySerializer(product, many=False)
        return Response(serializer.data)


    if request.method == "PUT":
        product.name = request.data['name']
        product.price = request.data['price']
        product.description = request.data['description']
        product.image = request.data['image']
        
        product.save()

        serializer = MySerializer(product, many = False)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        product.delete()
        return redirect('/')


    


