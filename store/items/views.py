from django.shortcuts import render
from django.views.generic import ListView
from .models import Glasses, Order
from django.template import Context, loader
from django.http import HttpResponse

class GlassesListView(ListView):
    model = Glasses
    context_object_name = 'glasses'
    template_name = 'items/stock.html'

def make_order(request, pk):
    glasses = Glasses.objects.get(pk=pk)
    quantity = request.POST.get('quantity')
    total_price = glasses.price * int(quantity)
    Order.objects.create(
        user=request.user,
        glasses=glasses,
        quantity=quantity,
        total_price=total_price
    )
    return render(request, 'items/order_confirmation.html', {'glasses': glasses, 'quantity': quantity, 'total_price': total_price})

def stock(request):
    return render(request, 'items/stock.html')

def index(request):
    return render(request, 'items/index.html')