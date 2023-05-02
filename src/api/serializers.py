from rest_framework import serializers
from olist.models import Customer, Order, Geolocation, OrderPayment, OrderItems


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('__all__')


class GeolocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geolocation
        fields = ('__all__')


class GeolocationTop10Serializer(serializers.ModelSerializer):

    class Meta:
        model = Geolocation
        fields = ('__all__')


class OrderPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderPayment
        fields = ('__all__')


class Chiffre_daffaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderPayment
        fields = ('__all__')


class Order_Item_Serializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = ('__all__')
