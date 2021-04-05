from ..models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'email', 'phone', 'first_name', 'last_name', 'is_active', 'is_staff', 'image']
