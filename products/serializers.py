from .models import Category, Product
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'slug', 'created_at', 'update_at')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('category', 'title', 'slug', 'description', 'price', 'available')