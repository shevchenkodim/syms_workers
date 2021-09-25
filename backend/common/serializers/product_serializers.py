from rest_framework import serializers
from common.products.product.product import Product


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'product_id', 'price', 'old_price', 'quantity', 'short_character']
