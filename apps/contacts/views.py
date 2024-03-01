from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

def index(request):
    return HttpResponse ("This is the Index Page")