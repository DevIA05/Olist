from rest_framework import routers
from api.views import CustomerSet

router = routers.DefaultRouter()
#Permet d'enregistrer nos différentes routes

router.register('clients', CustomerSet)