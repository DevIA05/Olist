
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('test', views.test, name="test"),
    path('charts', views.charts, name="charts"),
    path('general', views.GeneralTables, name="general"),
    path('data', views.DataTables, name="data"),
]