from django.urls import path

from .views import CategoryListCreateAPIView, ProductListCreateAPIView,  ProductRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name="list-create"),
    path('<pk:int>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name="ret...."),  # pk or int first?
    path('categories/', CategoryListCreateAPIView.as_view(), name="categories-list..."),
    path('categories/<id>/',)
]
