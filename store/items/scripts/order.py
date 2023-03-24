from .config import (
    render, redirect, messages, ListView)
from ..forms import OrdersForm
from ..models import Order

# Display all orders list
class OrdersListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'items/orders.html'


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
