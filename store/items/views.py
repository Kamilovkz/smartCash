from django.shortcuts import render
from django.http import HttpResponse
from .models import Stock
# Create your views here.

def index(request):
    latest_items_list = Stock.objects.order_by('-item_buying_date')[:5]
    output = ', '.join([i.item_name for i in latest_items_list])
    return HttpResponse(output)

def detail(request, item_id):
    return HttpResponse("You're looking at item %s" % item_id)

def results(request, item_id):
    response = "You're looking at the stock of items %s."
    return HttpResponse(response % item_id)

def vote(request, item_id):
    return HttpResponse("You're chosing on item %s." % item_id)