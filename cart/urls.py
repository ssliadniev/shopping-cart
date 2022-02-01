from django.urls import path

from cart.views import CartItemListCreateAPIView, CartItemUpdateDestroyAPIView


app_name = "cart"


urlpatterns = [
    path("", CartItemListCreateAPIView.as_view(), name="cart_item_list_create"),
    path(
        "<int:pk>/",
        CartItemUpdateDestroyAPIView.as_view(),
        name="cart_item_update_destroy",
    ),
]
