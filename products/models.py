from django.db import models


class Product(models):
    title = models.CharField(max_length=55)
    description = models.TextField()
    in_stock = models.BooleanField(blank=False)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Category(models):
    title = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.title
