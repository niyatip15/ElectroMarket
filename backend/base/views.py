from django.shortcuts import render
from .products import products
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getProducts(request):
    return Response(products)

@api_view(['GET'])
def getProduct(request,id):
    product = None
    for i in products:
        print(i,'=============')
        if i['_id'] == id:
            product = i
            print(product,'==========')
            break
    return Response(product)