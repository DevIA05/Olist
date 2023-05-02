
from django import template
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.template import loader
from django.db.models import Count, Avg, Sum, Max, Min
from olist.models import Customer, Order, Geolocation, OrderPayment, OrderItems
from api.serializers import CustomerSerializer, OrderSerializers, GeolocationSerializer, GeolocationTop10Serializer, Order_Item_Serializer, OrderPaymentSerializer, Chiffre_daffaireSerializer


class CustomerSet(ReadOnlyModelViewSet):
    # Je vais indiquer, quelles sont les données que je veux manipuler dans cette vue
    # Le [:100] me permet d'afficher seulement 10 résultats
    queryset = Customer.objects.all().order_by('zip_code_prefix')[:100]
    serializer_class = CustomerSerializer


class OrderViewset(ReadOnlyModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all().order_by('customer_id')[:100]

    # def list(self, request):
    #     return Response({})


class OrderTop10(ReadOnlyModelViewSet):
    serializer_class = OrderSerializers
    # Le [:10] me permet d'afficher seulement 10 résultats
    queryset = Order.objects.all()


class CustomerTop10(ReadOnlyModelViewSet):
    serializer_class = Order_Item_Serializer
    queryset = OrderItems.objects.values(
        'product_id').annotate(count=Count('product_id'))
    print("____________________________________________________________________________________________________________________")
    print(queryset)
    print("____________________________________________________________________________________________________________________")
    # Le order_by me permet de les ordonner de manière
    # queryset = Customer.objects.all().order_by('zip_code_prefix')[:10]
    # décroissante en fonction du zip_code_prefix, j'ai choisis le zip_code_prefix pour qu'il soit cohérent avec la class
    # CustomerSet


class GeolocationViewset(ReadOnlyModelViewSet):
    serializer_class = GeolocationSerializer
    # Celui-ci ainsi que GeolocationTop10 ont été ordonnés
    queryset = Geolocation.objects.all().order_by('geolocation_id')[:100]
    # en fonction du même champ c-a-d geolocation_id, dans un souci de cohérence visuelle


class GeolocationTop10(ReadOnlyModelViewSet):
    serializer_class = GeolocationTop10Serializer
    queryset = Geolocation.objects.all().order_by('geolocation_id')[:10]


class OrderPaymentViewset(ReadOnlyModelViewSet):
    serializer_class = OrderPaymentSerializer
    queryset = OrderPayment.objects.all().order_by('payment_value')[:100]


# Attention, cette classe n'est pas encore fonctionnelle
# Le lien http://127.0.0.1:8000/api/chiffre_daffaire/ mènera vers une erreur
class Chiffre_daffaire(ReadOnlyModelViewSet):
    serializer_class = Chiffre_daffaireSerializer
    queryset = OrderPayment.objects.all().aggregate(
        Sum('payment_value')).items()
