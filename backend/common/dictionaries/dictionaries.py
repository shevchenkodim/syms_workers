from django.db import models
from common.dictionaries.base import Dictionaries


class BrandDict(Dictionaries):
    """ Product brand dict model """
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dict_brand'
        ordering = ['value']


class UnitDict(Dictionaries):
    """ Unit dict model """

    class Meta:
        db_table = 'dict_unit'
        ordering = ['value']


class DictDeliveryMethods(Dictionaries):
    """ Delivery methods dict model """
    icon = models.CharField(max_length=100, default='mdi-truck-delivery-outline')

    class Meta:
        db_table = 'dict_delivery_methods'
        ordering = ['value']

    def do_json(self):
        return {**super(DictDeliveryMethods, self).do_json(), 'icons': self.icon}


class DictGuarantee(Dictionaries):
    """ Guarantee dict model """
    icon = models.CharField(max_length=100, default='mdi-security')

    class Meta:
        db_table = 'dict_guarantee'
        ordering = ['value']

    def do_json(self):
        return {**super(DictGuarantee, self).do_json(), 'icons': self.icon}


class DictPaymentMethods(Dictionaries):
    """ Payment methods dict model """
    icon = models.CharField(max_length=100, default='mdi-cash')

    class Meta:
        db_table = 'dict_payment_methods'
        ordering = ['value']

    def do_json(self):
        return {**super(DictPaymentMethods, self).do_json(), 'icons': self.icon}
