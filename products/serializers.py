from .models import Category, Product
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'title', 'slug')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'category', 'title', 'slug', 'description', 'price', 'available')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['category'] = {
            "pk": instance.category.pk,
            "title": instance.category.title
        }
        return ret
