from django.shortcuts import render
from django.views.generic import ListView
from .models import Glasses, Order
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")


def GlassesListView(ListView):
    model = Glasses
    context_object_name = 'glasses'
    template_name = 'store/index.html'
