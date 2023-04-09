
from django import template
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count, Avg, Sum, Max, Min
from olist.models import Customer, Order, Geolocation, OrderPayment
from api.serializers import CustomerSerializer, OrderSerializers, GeolocationSerializer, GeolocationTop10Serializer, OrderPaymentSerializer, Chiffre_daffaireSerializer


class CustomerSet(ReadOnlyModelViewSet):
    #Je vais indiquer, quelles sont les données que je veux manipuler dans cette vue
    queryset = Customer.objects.all().order_by('zip_code_prefix') #Le [:100] me permet d'afficher seulement 10 résultats
    serializer_class = CustomerSerializer


class OrderViewset(ReadOnlyModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all().order_by('customer_id')
    
    # def list(self, request):
    #     return Response({})

class OrderTop10(ReadOnlyModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all().order_by('customer_id')[:10] #Le [:10] me permet d'afficher seulement 10 résultats


class CustomerTop10(ReadOnlyModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all().order_by('zip_code_prefix')[:10] # Le order_by me permet de les ordonner  de manière
    # décroissante en fonction du zip_code_prefix, j'ai choisis le zip_code_prefix pour qu'il soit cohérent avec la class 
    # CustomerSet


class GeolocationViewset(ReadOnlyModelViewSet):
    serializer_class = GeolocationSerializer
    queryset = Geolocation.objects.all().order_by('geolocation_id')[:100] # Celui-ci ainsi que GeolocationTop10 ont été ordonnés
    # en fonction du même champ c-a-d geolocation_id, dans un souci de cohérence visuelle


class GeolocationTop10(ReadOnlyModelViewSet):
    serializer_class = GeolocationTop10Serializer
    queryset = Geolocation.objects.all().order_by('geolocation_id')[:10]


class OrderPaymentViewset(ReadOnlyModelViewSet):
    serializer_class = OrderPaymentSerializer
    queryset = OrderPayment.objects.all().order_by('payment_value')[:100]


class Chiffre_daffaire(ReadOnlyModelViewSet):
    serializer_class = Chiffre_daffaireSerializer
    preCA = OrderPayment.objects.all().aggregate(Sum('payment_value')).items()
    queryset = preCA
    print('__________________vvvv____________________')
    print('__________________________________________')
    print(type(queryset))
    print('__________________________________________')
    print('__________________^^^^____________________')

