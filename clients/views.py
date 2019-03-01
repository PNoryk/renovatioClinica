import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def homeView(request):
    return HttpResponseRedirect(reverse(getClients))


def getClients(request):
    data = {"api_key": "3971c1a15e8449ef7c5e0486471c63cd"}
    r = requests.post(r"https://app.rnova.org/api/public/getClinics", data=data)

    clients = r.json()['data']

    return render(request, "clients/getClients.html", context={"clients": clients})

