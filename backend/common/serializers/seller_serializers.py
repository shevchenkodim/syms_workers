from rest_framework import serializers
from common.seller.seller import SellerModel


class SellerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerModel
        fields = ['id', 'name', 'code_name', 'phone', 'address', 'address', 'schedule_work', 'email', 'image_logo']
