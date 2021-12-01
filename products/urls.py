from django.urls import path

from .views import (CategoryListCreateAPIView,
                    CategoryRetrieveUpdateDestroyAPIView,
                    ProductListCreateAPIView,
                    ProductRetrieveUpdateDestroyAPIView)

app_name = "product"

urlpatterns = [
    path("", ProductListCreateAPIView.as_view(), name="list-create"),
    path(
        "<int:pk>/",
        ProductRetrieveUpdateDestroyAPIView.as_view(),
        name="product-retrieve-update-destroy",
    ),
    path(
        "categories/",
        CategoryListCreateAPIView.as_view(),
        name="category-list-create",
    ),
    path(
        "categories/<int:pk>/",
        CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category-retrieve-update-destroy",
    ),
]
