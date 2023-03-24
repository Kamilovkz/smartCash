from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import GlassesForm, OrdersForm
from .models import Glasses, Order
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

# Add glasses to stock 
def add_stock(request):
    if request.method == 'POST':
        form = GlassesForm(request.POST)
        if form.is_valid():
            glasses_count = Glasses.objects.filter(type='glasses').count()
            print(glasses_count)
            form.save()
            messages.success(request, f"{form.cleaned_data['name']} glasses was added successfully!")
            return redirect('/stock/')
    else:
        form = GlassesForm()
    return render(request, 'items/add_stock.html', {'form': form})

# Add orders to Database
def add_order(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            # Retrieve the glasses info
            glasses = form.cleaned_data['glasses']
            quantity = form.cleaned_data['quantity']
            if form.cleaned_data['discount'] > 0:
                discount = (glasses.price / 100) * form.cleaned_data['discount']
                total_price = (glasses.price - discount) * quantity 
            else:
                total_price = glasses.price * quantity
            if glasses.stock - quantity < 0:
                messages.warning(request, f"There is no such amount in the database. There are only {glasses.stock} pairs")
            else:
                glasses.stock -= quantity
                glasses.save()

                # Create and save the Order object
                order = form.save(commit=False)
                order.total_price = total_price
                order.save()
                messages.success(request, f"{form.cleaned_data['glasses']} glasses was added!")
                return redirect('/orders/')
    else:
        form = OrdersForm
    return render(request, 'items/add_order.html', {'form': form})

# Deleting Stock items and redirect to Stock page
def delete_item(request, pk):
    display_item = Glasses.objects.get(id=pk)
    display_item.delete()
    # show_stock(request)
    return redirect('/stock/')

# Update a order
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrdersForm(instance=order)
    if request.method == 'POST':
        form = OrdersForm(request.POST, instance=order)
        if form.is_valid():
            inital_quantity = form['quantity'].initial
            order.update_stock(inital_quantity)
            order.calculate_total_price()
            form.save()
            messages.success(request, f"{form.cleaned_data['glasses']} was changed successfully!")
            return redirect('/orders/')
    context = {'form': form}
    return render(request, "items/add_order.html", context)

# The main page
def index(request):
    return render(request, 'items/index.html')

