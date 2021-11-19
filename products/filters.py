import django_filters
from django.db.models import Q
from products.models import Product


class ProductFilters(django_filters.FilterSet):
    price_from = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_to = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    search = django_filters.CharFilter(method="filter_search")

    class Meta:
        model = Product
        fields = ["in_stock", "price_from", "price_to", "search"]

    @staticmethod
    def filter_search(queryset, values, *args, **kwargs):
        values = values.split(" ") if values else []
        for value in values:
            queryset = queryset.filter(
                Q(title__incontains=value) |
                Q(category__title_incontains=value)
            )
        return queryset
