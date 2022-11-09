from django.shortcuts import render
from django.http import  HttpResponse
from .models import Client
from django.views import generic

class ListClientView(generic.ListView):
    model = Client
    template_name = 'client_view.html'
    context_object_name = 'clients'


class DetailClientView(generic.DetailView):
    model = Client
    template_name = 'detail_client.html'
    context_object_name = 'client'