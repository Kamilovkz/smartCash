from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Glasses, Order
from django.template import Context, loader
from django.http import HttpResponse
from django import forms

# Display all glasses list
class GlassesListView(ListView):
    model = Glasses
    context_object_name = 'glasses'
    template_name = 'items/stock.html'

# Display all orders list
class OrdersListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'items/orders.html'

# Form class for input data (add glasses)
class GlassesForm(forms.ModelForm):
    class Meta:
        model = Glasses
        fields = ['name', 'type', 'model', 'size', 'country', 'price', 'stock']

def add_stock(request):
    if request.method == 'POST':
        form = GlassesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = GlassesForm()
    return render(request, 'items/add_stock.html', {'form': form})


def index(request):
    return render(request, 'items/index.html')

def about(request):
    return render(request, 'items/about.html')

# We need changes here
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
