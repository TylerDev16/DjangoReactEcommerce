from django.shortcuts import render
from django.http import JsonResponse
from .products import products

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['GET'])
def get_routes(request):
    routes = [
        'api/products/',
        'api/products/create/',
        'api/products/upload/',

        'api/products/<int:id>/reviews/',

        'api/products/top/',
        'api/products/<int:id>/',

        'api/products/delete/<int:id>/',
        'api/products/update/<int:id>/',
    ]
    return Response(routes)


@api_view(['GET'])
def get_products(request):
    return Response(products)


@api_view(['GET'])
def get_product(request, pk):
    product = None

    for p in products:
        if p['_id'] == pk:
            product = p
            break

    return Response(product)