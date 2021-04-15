from django.db import models
from common.seo.seo import SeoModel


class SellerModel(SeoModel):
    """ Seller model """
    name = models.CharField(max_length=125, unique=True, db_index=True, verbose_name='Seller name')
    code_name = models.CharField(max_length=125, unique=True, db_index=True, verbose_name='Seller code')
    phone = models.CharField(max_length=20, unique=True, default='+380000000000', verbose_name='Phone')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Address')  # Create model Address
    schedule_work = models.TextField(blank=True, verbose_name='Schedule work')
    email = models.EmailField(default='default@gmail.com', unique=True, verbose_name='Email')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date updated')
    image_logo = models.ImageField(upload_to='seller/logo', blank=True, null=True, verbose_name='Logo')

    class Meta:
        db_table = 'seller'
        ordering = ['name']

    def __str__(self):
        return self.name
