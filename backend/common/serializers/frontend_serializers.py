from rest_framework import serializers
from common.products.categories.categories import CategoryModel
from common.frontend.sliders.main_slider import MainCarouselModel


class MainCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCarouselModel
        fields = ['id', 'order_id', 'item_alt', 'item_image']


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'code_name', 'icon', 'is_active', 'description']

