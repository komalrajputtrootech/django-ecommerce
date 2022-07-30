from django.shortcuts import render

from rest_framework import viewsets, filters
from django_filters import rest_framework as r_filters

from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (r_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter, )
    filterset_fields = ('category__slug',)
    ordering_fields = ('price',)
    search_fields = ["price", "name", "description"]


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "slug"

