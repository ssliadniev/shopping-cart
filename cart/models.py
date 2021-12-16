from django.db import models

from products.models import Product
from user.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("user",)

    def total(self):
        total_prod = CartItem.objects.filter(cart=self)
        return sum([i.product.price * i.quantity for i in total_prod])

    def __str__(self):
        return self.user


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"
        ordering = ("cart",)

    def get_sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return "{}: {}".format(self.cart, self.product)
