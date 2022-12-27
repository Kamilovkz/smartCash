from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello Django. You are at the items index.")

def detail(request, item_id):
    return HttpResponse("You're looking at item %s" % item_id)

def results(request, item_id):
    response = "You're looking at the stock of items %s."
    return HttpResponse(response % item_id)

def vote(request, item_id):
    return HttpResponse("You're chosing on item %s." % item_id)