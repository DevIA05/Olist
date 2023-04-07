from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from olist.models import CustomerIds
from api.serializers import CustomersIdsSerializer



class CustomerSet(ReadOnlyModelViewSet):
    #Je vais indiquer, quelles sont les données que je veux manipuler dans cette vue
    queryset = CustomerIds.objects.all()
    serializer_class = CustomersIdsSerializer
