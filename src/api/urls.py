from rest_framework import routers
from api.views import CustomerSet, OrderViewset, OrderTop10, CustomerTop10, GeolocationViewset, GeolocationTop10, OrderPaymentViewset

router = routers.DefaultRouter()
#Permet d'enregistrer nos différentes routes

router.register('customers', CustomerSet),
router.register(r'customerTOP10', CustomerTop10, basename='CustomerTOP10'),
router.register(r'orders', OrderViewset, basename='Order'),
router.register(r'orderTOP10', OrderTop10, basename='TOP10'),
router.register(r'geolocation', GeolocationViewset, basename='geolocation'),
router.register(r'geolocationTop10', GeolocationTop10, basename='geolocationTop10'),
router.register(r'orderPayment', OrderPaymentViewset, basename='orderPayment'),
