from .config import (
    render, redirect, messages, ListView)
from ..forms import GlassesForm
from ..models import Glasses

# Display all glasses list
class GlassesListView(ListView):
    model = Glasses
    context_object_name = 'glasses'
    template_name = 'items/stock.html'

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

# Deleting Stock items and redirect to Stock page
def delete_stock_item(request, pk):
    display_item = Glasses.objects.get(id=pk)
    display_item.delete()
    return redirect('/stock/')
