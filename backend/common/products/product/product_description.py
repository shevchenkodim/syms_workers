from django.db import models
from common.products.product.product import Product


class ProductDescription(models.Model):
    """ Product description model """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    order_id = models.IntegerField(default=0, verbose_name='Order id')

    class Meta:
        db_table = 'product_description'
        ordering = ['order_id']

    def __str__(self):
        return self.title

    @staticmethod
    def get_description_by_product(product_id):
        return [{
            'title': description.title,
            'description': description.description
        } for description in ProductDescription.objects.filter(product__id=product_id)]
