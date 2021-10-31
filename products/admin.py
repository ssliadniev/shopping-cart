from django.contrib import admin

from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("title", "category", "available", "in_stock")
    list_filter = ["category"]
    search_fields = (
        "title",
        "category",
        "in_stock"
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("title", "created_at", "updated_at")
    list_filter = ["title"]
    search_fields = (
        "title",
    )
