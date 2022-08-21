from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>',
    }

    return Response(api_urls)


@csrf_exempt
@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def viewProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def createProduct(request):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product delete succes')
