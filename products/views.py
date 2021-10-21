from .models import Category, Product
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


