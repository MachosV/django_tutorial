from django.shortcuts import render
from django.views import generic

# Create your views here.

class indexView(generic.View):
    template_name = 'pizzeria/details.html'