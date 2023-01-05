from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Glasses, Order
from django.template import Context, loader
from django.http import HttpResponse
from django import forms
from django.contrib import messages

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

# Form for input data (add glasses)
class GlassesForm(forms.ModelForm):
    class Meta:
        model = Glasses
        fields = ['name', 'type', 'model', 'size', 'country', 'price', 'stock']

# Add glasses to stock 
def add_stock(request):
    if request.method == 'POST':
        form = GlassesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"{form.cleaned_data['name']}")
            return redirect('/stock/')
    else:
        form = GlassesForm()
    return render(request, 'items/add_stock.html', {'form': form})

# Form for input data (add orders)
class OrdersForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'glasses', 'quantity', 'status']
# Add orders to Database
def add_order(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            # Retrieve the glasses info
            glasses = form.cleaned_data['glasses']
            quantity = form.cleaned_data['quantity']
            total_price = glasses.price * quantity
            glasses.stock -= quantity
            glasses.save()

            # Create and save the Order object
            order = form.save(commit=False)
            order.total_price = total_price
            order.save()
            return redirect('/orders/')
    else:
        form = OrdersForm
    return render(request, 'items/add_order.html', {'form': form})


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
