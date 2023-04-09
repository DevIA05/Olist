from rest_framework import routers
from api.views import CustomerSet, OrderViewset, OrderTop10, CustomerTop10

router = routers.DefaultRouter()
#Permet d'enregistrer nos différentes routes

router.register('clients', CustomerSet),
router.register(r'orders', OrderViewset, basename='order'),
router.register(r'TOP10', OrderTop10, basename='TOP10')
router.register(r'CustomerTOP10', CustomerTop10, basename='CustomerTOP10')
