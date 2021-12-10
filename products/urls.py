from django.urls import path

from .views import (CategoryListCreateAPIView,
                    CategoryRetrieveUpdateDestroyAPIView,
                    ProductListAPIView,
                    ProductRetrieveUpdateDestroyAPIView,
                    AdminProductListCreateAPIView)

app_name = "product"

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="list"),
    path(
        "admin/",
        AdminProductListCreateAPIView.as_view(),
        name="admin-create-product",
    ),
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
