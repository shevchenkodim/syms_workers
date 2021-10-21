from django.db import models
from django.conf import settings
from common.products.product.product import Product
from common.seller.seller import SellerDeliveryMethods
from common.dictionaries.dictionaries import DictDeliveryMethods
from common.serializers.product_serializers import ProductModelSerializer


class CartItems(models.Model):
    """ Model for items in client cart """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Client')
    count = models.IntegerField(default=1, verbose_name='Count')
    delivery_method = models.ForeignKey(DictDeliveryMethods, default=1, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    def __str__(self):
        return f'{self.product.__str__()}'

    def get_item_json(self) -> dict:
        return {
            'id': self.id,
            'quantity': self.count,
            'price': self.product.price.__str__(),
            'product': ProductModelSerializer(self.product).data,
            'seller_code': self.product.seller.code_name,
            'delivery_method': self.delivery_method.id,
            'delivery_methods': [{
                'id': x.id,
                'value': x.delivery_methods.value
            } for x in SellerDeliveryMethods.objects.filter(seller=self.product.seller)]
        }

    @staticmethod
    def client_has_cart_item(product_id, client):
        return CartItems.objects.filter(product__product_id=product_id, client=client).exists()

    @staticmethod
    def get_len_items(client):
        return CartItems.objects.filter(client=client).count()
