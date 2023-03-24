from .config import render

def about(request):
    return render(request, 'items/about.html')
