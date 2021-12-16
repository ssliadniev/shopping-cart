# Generated by Django 3.2 on 2021-12-13 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def create_cart_for_user(apps, schema_editor):
    users = apps.get_model("user", "User")
    cart = apps.get_model("cart", "Cart")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
    print(users.objects.all())
    for user in users.objects.all():
        print(user)
        cart.objects.create(user__id=user.id)
        cart.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'ordering': ('cart',),
            },
        ),
        migrations.RunPython(create_cart_for_user)
    ]
