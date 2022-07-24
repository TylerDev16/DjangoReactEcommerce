from django.urls import path
from .views import *


urlpatterns = [
    path('', get_routes, name='getRoutes'),
    path('products/', get_products, name='getProducts'),
    path('products/<str:pk>/', get_product, name='getProducts'),
]