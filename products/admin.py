from django.contrib import admin

from products.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information about product',
         {'fields': ['title', 'description', 'in_stock', 'slug', 'price']})
    ]
    list_display = ('title', 'description', 'in_stock', 'slug', 'price')
    list_filter = ['in_stock']
    search_fields = ['title', 'slug']


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information about category',
         {'fields': ['title', 'description']})
    ]
    list_display = ('title', 'description')
    list_filter = ['title']
    search_fields = ['title']
    actions = ['delete_selected']

    def has_delete_permission(self, request, obj=None):
        return False

    def delete_selected(self, request, queryset):
        queryset.update(is_abort=True)

    delete_selected.short_description = "Delete selected item"


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
