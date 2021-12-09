from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from cart.models import Cart, CartItem


class CartItemListCreateAPIView(ListCreateAPIView):
    queryset = CartItem.objects.all()

    #total

class CartItemUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    queryset = CartItem.objects.all()
