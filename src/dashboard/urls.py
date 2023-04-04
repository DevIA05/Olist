
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('component', views.component_alert, name="ca"),

]