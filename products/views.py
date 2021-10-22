from .models import Category, Product
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from serializers import CategorySerializer, ProductSerializer
from django.shortcuts import render, get_object_or_404


class CategoryListCreateAPIView(ListCreateAPIView):
    categories = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return get_object_or_404(self.categories)


class ProductListCreateAPIView(ListCreateAPIView):
    products = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]

    def get_product_list(self, category=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category:
            products = products.filter(slug=category)
        return products


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    products = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]

    def get_product_detail(self, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        return product
