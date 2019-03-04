from django.urls import path

from clients.views import *

urlpatterns = [
    path("", homeView, name="home"),
    path("clients/", clientsView, name="getClients"),
    path("professions/", professionsView, name="getProfessions"),
    path("users/", UsersFormView.as_view(), name="getUsers"),
    path("users/list/<int:clinic_id>/<int:profession_id>/", usersView, name="usersList"),
    path("users/list/<int:clinic_id>/<int:profession_id>/<int:role>", usersView, name="usersList"),

]
