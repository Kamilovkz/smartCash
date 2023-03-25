from .config import render, model_to_dict
from ..models import Order

def reports(request):
    queryset = Order.objects.all().values()
    context = {'data': queryset}
    print(context)
    return render(request, './items/reports.html', context)