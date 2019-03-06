from django.urls import path

from clients.views import *

urlpatterns = [
    path("", homeView, name="home"),
    path("clients/", clientsView, name="getClients"),
    path("professions/", professionsView, name="getProfessions"),
    path("users/", UsersFormView.as_view(), name="getUsers"),

    path("users/list/<int:clinic_id>/<int:profession_id>/", usersView, name="usersList"),
    path("users/list/<int:clinic_id>/<int:profession_id>/<role>/", usersView, name="usersList"),

    path("schedule/", ScheduleFormView.as_view(), name="getSchedule"),
    path("schedule/list/<int:clinic_id>/<int:user_id>/<slug:time_start>/<slug:time_end>/<int:step>/",
         scheduleView, name="scheduleList"),
]
