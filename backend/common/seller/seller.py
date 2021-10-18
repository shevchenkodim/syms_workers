from django.db import models

from common.dictionaries.dictionaries import DictDeliveryMethods, DictGuarantee, DictPaymentMethods
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


class SellerDeliveryMethods(models.Model):
    """ Seller delivery """
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    delivery_methods = models.ForeignKey(DictDeliveryMethods, on_delete=models.CASCADE)

    class Meta:
        db_table = 'seller_delivery_methods'
        ordering = ['pk']

    def __str__(self):
        return self.pk.__str__()


class SellerGuarantee(models.Model):
    """ Seller guarantee """
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    guarantee = models.ForeignKey(DictGuarantee, on_delete=models.CASCADE)

    class Meta:
        db_table = 'seller_guarantee'
        ordering = ['pk']

    def __str__(self):
        return self.pk.__str__()


class SellerPaymentMethods(models.Model):
    """ Seller payment methods """
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    payment_methods = models.ForeignKey(DictPaymentMethods, on_delete=models.CASCADE)

    class Meta:
        db_table = 'seller_payment_methods'
        ordering = ['pk']

    def __str__(self):
        return self.pk.__str__()
