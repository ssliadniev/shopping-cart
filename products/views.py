from .models import Category, Product
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404


class CategoryDetailView(DetailView):
    model = Category

    categories = Category.objects.all()
