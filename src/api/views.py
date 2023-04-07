
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from olist.models import Customer, Order
from rest_framework.decorators import action
from api.serializers import CustomerSerializer, OrderSerializers



class CustomerSet(ReadOnlyModelViewSet):
    #Je vais indiquer, quelles sont les données que je veux manipuler dans cette vue
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewset(ReadOnlyModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()

    def list(self, request):
        print('Morue')
        return Response({})
