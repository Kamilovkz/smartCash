from .config import render, model_to_dict
from items.models import Order


def reports(request):
    reports_data = Order.objects.all()
    return render(request, "./items/reports.html", {"reports": reports_data})
