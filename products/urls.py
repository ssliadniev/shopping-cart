from django.urls import path

from .views import CategoryListCreateAPIView, ProductListCreateAPIView,  ProductRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name="list-create"),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name="retrieve-update-destroy"),
    path('categories/', CategoryListCreateAPIView.as_view(), name="categories-list-create"),
    path('categories/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name="retrieve-update-destroy")
]
