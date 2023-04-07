from rest_framework import serializers
from olist.models import Customer, Order


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('order_approved_at', 'customer_id')
