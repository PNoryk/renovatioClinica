from django.urls import path

from clients.views import homeView, getClients

urlpatterns = [
    path("", homeView, name="home"),
    path("getClients/", getClients, name="getClients")
]