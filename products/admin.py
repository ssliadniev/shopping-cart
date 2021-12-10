from django.contrib import admin

from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("title", "category", "available", "in_stock")
    list_filter = ["category", "available"]
    search_fields = (
        "title",
        "category__title",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("title",)
    search_fields = (
        "title",
    )
