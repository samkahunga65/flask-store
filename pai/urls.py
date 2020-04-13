from django.urls import path, include
from . import views

urlpatterns = [
    path('/v1/on-covid-19/json', views.covid, name='covid'),
    path('/v1/on-covid-19/xml', views.covidx, name='covid'),
]
