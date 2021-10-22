from .models import Category, Product
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from serializers import CategorySerializer, ProductSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
