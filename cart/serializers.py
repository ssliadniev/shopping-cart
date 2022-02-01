from rest_framework.serializers import ModelSerializer

from cart.models import CartItem
from products.models import Product


class ProductSerializer(ModelSerializer):
    """
    ProductSerializer is used in CartItemSerializer to extract some product attributes
    and add them to cart_item.
    """

    class Meta:
        model = Product
        fields = ("pk", "title", "image")


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("cart", "product", "quantity")

    def update(self, instance, validated_data):
        validated_data.pop("cart")
        validated_data.pop("product")
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super(CartItemSerializer, self).to_representation(instance)
        representation["sub_total"] = instance.get_sub_total()
        representation["product"] = ProductSerializer(instance.product).data
        return representation
