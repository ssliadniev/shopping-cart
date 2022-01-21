from rest_framework.generics import DestroyAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response

from cart.models import CartItem
from cart.serializers import CartItemSerializer


class CartItemListCreateAPIView(ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            {"result": response.data, "total_amount": request.user.cart.total()}
        )

    def create(self, request, *args, **kwargs):
        request.data["cart"] = request.user.cart
        return super().create(request, *args, **kwargs)


class CartItemUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)
