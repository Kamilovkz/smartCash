from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Glasses, Order
from django.template import Context, loader
from django.http import HttpResponseNotAllowed
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
            messages.success(request, f"{form.cleaned_data['name']} glasses was added successfully!")
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
            messages.success(request, f"{form.cleaned_data['glasses']}")
            return redirect('/orders/')
    else:
        form = OrdersForm
    return render(request, 'items/add_order.html', {'form': form})


def delete_stock(request):
    if request.method == 'DELETE':
        form = GlassesForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Glasses.objects.filter(name=name).delete()
            messages.success(request, f"{name} deleted")
            return redirect('/stock/')
    else:
        return HttpResponseNotAllowed(['DELETE'])


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrdersForm(instance=order)
    if request.method == 'POST':
        form = OrdersForm(request.POST, instance=order)
        if form.is_valid():
            inital_quantity = form['quantity'].initial
            order.update_stock(inital_quantity)
            form.save()
            messages.success(request, f"{form.cleaned_data['glasses']} was changed successfully!")
            return redirect('/orders/')
    context = {'form': form}
    return render(request, "items/add_order.html", context)




def about(request):
    return render(request, 'items/about.html')
def index(request):
    return render(request, 'items/index.html')

# We need changes here
def make_order(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            glasses = Glasses.objects.get(pk=form.cleaned_data['name'])
            order = Order(
                glasses = glasses,
                quantity=form.cleaned_data['quantity'],
                total_price=glasses.price * form.cleaned_data['quantity'],
                user = request.user
            )
            order.save()
    else:
        form = OrdersForm()
    orders = Order.objects.filter(user=request.user)
    glasses = Glasses.objects.all()
    return render (request, 'items/index.html', {'form': form, 'orders': orders, 'glasses': glasses})