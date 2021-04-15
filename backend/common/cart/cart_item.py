from django.db import models
from django.conf import settings
from common.products.product.product import Product


class CartItems(models.Model):
    """ Model for items in client cart """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Client')
    count = models.IntegerField(default=1, verbose_name='Count')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    def __str__(self):
        return f'{self.product.__str__()}'

    def get_item_json(self) -> dict:
        return {
            'quantity': self.count,
            'product_id': self.product.product_id,
            'price': self.product.price.__str__()
        }

    @staticmethod
    def client_has_cart_item(product_id, client):
        return CartItems.objects.filter(product__product_id=product_id, client=client).exists()

    @staticmethod
    def get_len_items(client):
        return CartItems.objects.filter(client=client).count()
