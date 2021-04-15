from django.db import models
from common.products.product.product import Product


class ProductImage(models.Model):
    """ Product image model """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    image = models.ImageField(upload_to='product/image', verbose_name='Image')
    item_alt = models.CharField(max_length=100, blank=True, verbose_name='Image description')
    order_id = models.IntegerField(default=0, verbose_name='Order id')

    class Meta:
        db_table = 'product_image'
        ordering = ['order_id']

    def __str__(self):
        return self.image.url

    @staticmethod
    def get_images_by_product(product_id):
        return [{'url': image.image.url} for image in ProductImage.objects.filter(product__id=product_id)]
