from django.db import models

from products.models import Product
from user.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")

    class Meta:
        ordering = ("user",)

    def total(self):
        return sum([cart_item.get_sub_total() for cart_item in self.cart_items])

    def __str__(self):
        return self.user


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"
        ordering = ("cart",)

    def get_sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return "{}: {}".format(self.cart, self.product)
