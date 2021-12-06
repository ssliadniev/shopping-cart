from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from cart.models import Cart, CartItem


class CartListCreateAPIView(ListCreateAPIView):
    queryset = Cart.objects.all()


class CartRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()


class CartItemListCreateAPIView(ListCreateAPIView):
    queryset = CartItem.objects.all()


class CartItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
