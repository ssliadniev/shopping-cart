from django.db import models


class Product(models):
    title = models.CharField(max_length=55)
    description = models.TextField()
    in_stock = models.BooleanField(blank=False)
    slug = models.CharField(max_length=150)
    price = models.FloatField()


class Category(models):
    title = models.CharField(max_length=40)
    description = models.TextField()
