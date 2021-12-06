import django_filters
from django.db.models import Q
from products.models import Product


class ProductFilters(django_filters.FilterSet):
    price_from = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_to = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    search = django_filters.CharFilter(method="filter_search")
    is_in_stock = django_filters.BooleanFilter(method="filter_in_stock")

    class Meta:
        model = Product
        fields = ["price_from", "price_to", "search", "is_in_stock"]

    @staticmethod
    def filter_search(queryset, values, *args, **kwargs):
        values = values.split(" ") if values else []
        print(values)
        for value in values:
            queryset = queryset.filter(
                Q(title__icontains=value) |
                Q(category__title__icontains=value)
            )
        return queryset

    @staticmethod
    def filter_in_stock(queryset, value, *args, **kwargs):
        if value:
            return queryset.filter(in_stock__gt=0)
        return queryset.filter(in_stock=0)
