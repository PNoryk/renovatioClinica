import pprint

from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from clients import dataRequests
from clients.forms import UsersForm


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
        pprint.pprint(form.cleaned_data)
        clinic_id = form.cleaned_data["clinic_id"]
        profession_id = form.cleaned_data["profession_id"]

        self.success_url = r"list/{}/{}/".format(clinic_id, profession_id)

        return super().form_valid(form)
