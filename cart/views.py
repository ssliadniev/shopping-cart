from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from cart.models import Cart, CartItem
from cart.serializers import CartItemSerializer


class CartItemListCreateAPIView(ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        #return Response({"result": serializer.data, "total_amount": queryset.user})


class CartItemUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)
