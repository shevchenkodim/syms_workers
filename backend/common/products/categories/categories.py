from django.db import models
from common.seo.seo import SeoModel


class CategoryModel(SeoModel):
    """ Categories MPTTModel models """
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Category name')
    code_name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Category code')
    slug = models.SlugField(max_length=125, unique=True, verbose_name='Slug')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    is_active = models.BooleanField(default=True, verbose_name='Is active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date updated')
    icon = models.CharField(max_length=50, verbose_name='Icon')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='parent_item')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        ordering = ['name', '-created_at']
