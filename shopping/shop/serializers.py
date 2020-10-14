from rest_framework import serializers
from . import models
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many = True)
    class Meta:
        model = models.Order
        fields = ('finised','items')