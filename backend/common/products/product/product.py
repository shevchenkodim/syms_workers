from django.db import models
from common.seo.seo import SeoModel
from common.seller.seller import SellerModel
from common.dictionaries.dictionaries import BrandDict
from common.products.categories.categories import CategoryModel


class AvailableProductManager(models.Manager):
    def get_queryset(self):
        return super(AvailableProductManager, self).get_queryset()\
            .filter(is_active=True, is_available=True, quantity__gt=0)


class Product(SeoModel):
    """ Product model """
    name = models.CharField(max_length=255, verbose_name='Product name')
    code = models.CharField(max_length=255, unique=True, verbose_name='Product code')
    product_id = models.CharField(max_length=55, unique=True, db_index=True, verbose_name='product_id')
    is_available = models.BooleanField(default=True, verbose_name='Available')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Price')
    old_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, verbose_name='Old price')
    is_active = models.BooleanField(default=True, verbose_name='Is active')
    quantity = models.IntegerField(default=0, verbose_name='Quantity')
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date updated')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name='Category')
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE, verbose_name='Seller')
    brand = models.ForeignKey(BrandDict, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Brand')
    short_character = models.CharField(max_length=255, null=True, blank=True, verbose_name='Short character')

    objects = models.Manager()
    available = AvailableProductManager()

    class Meta:
        db_table = 'product'
        ordering = ['created_at']

    @property
    def is_available_product(self):
        return all([self.is_available, self.is_active, self.quantity > 0])

    def __str__(self):
        return self.product_id

    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product_id = generate_product_id()
        super(Product, self).save(*args, **kwargs)


def generate_product_id():
    """ Generate new product_id on create """
    last_product = Product.objects.all().order_by('created_at').last()
    last_value = last_product.product_id if last_product else '0000000000'
    value_int = int(last_value) + 1
    value_len = len(str(value_int))
    return last_value[:-value_len] + str(value_int)
