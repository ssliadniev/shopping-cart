import django_filters
from products.models import Product


class ProductFilters(django_filters.FilterSet):
    price_from = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_to = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ["in_stock", "price_from", "price_to"]
        # Q search fields
