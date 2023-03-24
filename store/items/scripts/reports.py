from .config import render

def reports(request):
    return render(request, './items/reports.html')