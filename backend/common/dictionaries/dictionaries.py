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
