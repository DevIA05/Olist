
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from olist.models import Customer, Order
from api.serializers import CustomerSerializer, OrderSerializers


class CustomerSet(viewsets.ModelViewSet):
    #Je vais indiquer, quelles sont les données que je veux manipuler dans cette vue
    queryset = Customer.objects.all() #Le [:100] me permet d'afficher seulement 10 résultats
    serializer_class = CustomerSerializer


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
    
    # def list(self, request):
    #     return Response({})
class OrderTop10(ReadOnlyModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()[:10] #Le [:10] me permet d'afficher seulement 10 résultats

class CustomerTop10(ReadOnlyModelViewSet):
    queryset = Customer.objects.all()[:10]
    serializer_class = CustomerSerializer
    