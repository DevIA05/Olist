from rest_framework import serializers
from olist.models import CustomerIds


class CustomersIdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerIds
        fields = '__all__'