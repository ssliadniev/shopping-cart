from django.urls import path

from cart.views import (CartItemListCreateAPIView,
                        CartItemRetrieveUpdateDestroyAPIView,
                        CartListCreateAPIView,
                        CartRetrieveUpdateDestroyAPIView)

app_name = "cart"


urlpatterns = [
    path("cart/", CartListCreateAPIView.as_view(), name="cart-list-create"),
    path(
        "<int:pk>/",
        CartRetrieveUpdateDestroyAPIView.as_view(),
        name="cart-retrieve-update-destroy",
    ),
    path(
        "cart_item/", CartItemListCreateAPIView.as_view(), name="cart_item-list-create"
    ),
    path(
        "cart_item/<int:pk>/",
        CartItemRetrieveUpdateDestroyAPIView.as_view(),
        name="cart_item-retrieve-update-destroy",
    ),
]
