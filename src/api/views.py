from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from olist.models import Customer
from api.serializers import CustomerSerializer



class CustomerSet(ReadOnlyModelViewSet):
    #Je vais indiquer, quelles sont les données que je veux manipuler dans cette vue
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
