from django.db import models
from django.conf import settings
from common.cart.cart import client_cart
from common.cart.cart_item import CartItems
from common.products.product.product import Product
from common.dictionaries.dictionaries import DictOrderStatus, DictDeliveryMethods


class Order(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Client')
    status = models.ForeignKey(DictOrderStatus, on_delete=models.CASCADE, verbose_name='Status')
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Total amount')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date updated')

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.pk.__str__()

    @staticmethod
    def create_order(client, cart_items: [CartItems], status='new'):
        order_db = Order(client=client, total_amount=client_cart.get_total_price(client))
        order_db.status = DictOrderStatus.objects.get_or_create(value='NEW', code='new')[0]
        order_db.save()

        for item in cart_items:
            OrderItems.objects.create(
                order=order_db,
                product=item.product,
                count=item.count,
                delivery_method=item.delivery_method
            )

        CartItems.objects.filter(id__in=[x.id for x in cart_items]).delete()


class OrderItems(models.Model):
    """ Model for items in client order """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product', related_name='base_order')
    count = models.IntegerField(default=1, verbose_name='Count')
    delivery_method = models.ForeignKey(DictDeliveryMethods, default=1, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    def __str__(self):
        return f'{self.product.__str__()}'
