from rest_framework import routers
from api.views import CustomerSet, OrderViewset

router = routers.DefaultRouter()
#Permet d'enregistrer nos différentes routes

router.register('clients', CustomerSet),
router.register(r'orders', OrderViewset, basename='order')
