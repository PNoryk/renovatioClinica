from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from clients import dataRequests
from clients.forms import UsersForm, ScheduleForm


def homeView(request):
    return HttpResponseRedirect(reverse(clientsView))


def clientsView(request):
    clients = dataRequests.getClinics()
    return render(request, "clients/clients.html", context={"clients": clients["data"]})


def professionsView(request):
    professions = dataRequests.getProfessions()
    return render(request, "clients/professions.html", context={"professions": professions["data"]})


def usersView(request, clinic_id, profession_id, role=""):
    users = dataRequests.getUsers(clinic_id, profession_id, role)
    return render(request, "clients/users-list.html", context={"users": users["data"]})


class UsersFormView(views.generic.FormView):
    form_class = UsersForm
    template_name = "clients/users.html"

    def form_valid(self, form):
        clinic_id = form.cleaned_data["clinic_id"]
        profession_id = form.cleaned_data["profession_id"]
        self.success_url = r"list/{}/{}/".format(clinic_id, profession_id)

        role = form.cleaned_data["role"]
        if role:
            self.success_url += f"{role}/"

        return super().form_valid(form)


class ScheduleFormView(views.generic.FormView):
    form_class = ScheduleForm
    template_name = "clients/schedule.html"

    def form_valid(self, form):
        clinic_id = form.cleaned_data["clinic_id"]
        user_id = form.cleaned_data["user_id"]
        time_start = form.cleaned_data["time_start"]
        time_end = form.cleaned_data["time_end"]
        step = form.cleaned_data["step"]

        self.success_url = "list/{}/{}/{}/{}/{}/".format(clinic_id, user_id, time_start, time_end, step)

        return super().form_valid(form)


def scheduleView(request, clinic_id, user_id, time_start, time_end, step):
    schedule = dataRequests.getSchedule(clinic_id, user_id, time_start, time_end, step)
    return render(request, "clients/schedule-list.html", context={"schedule": schedule["data"]})
