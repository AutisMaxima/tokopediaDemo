from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'image_link',
            'product_name',
            'price',
            'seller'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'phone_number',
            'customer_name',
            'age',
            'email_address'
        ]


class AutoBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoBuy
        fields = [
            'id',
            'customer',
            'product',
            'start_date',
            'reminder_cycle',
            'is_autobuy'
        ]
