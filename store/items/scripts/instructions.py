from .config import render

def instructions(request):
    return render(request, 'items/instructions.html')
