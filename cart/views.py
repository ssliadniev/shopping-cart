from rest_framework.generics import (DestroyAPIView, ListCreateAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import CartItem
from cart.serializers import CartItemSerializer


class CartItemListCreateAPIView(ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user.id)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            {"result": response.data, "total_amount": request.user.cart.total()}
        )

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data["cart"] = request.user.cart
        request.data._mutable = False
        return super().create(request, *args, **kwargs)


class CartItemUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user.id)
