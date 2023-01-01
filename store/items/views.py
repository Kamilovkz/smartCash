from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Stock, Product
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.

def index(request):
    latest_items_list = Stock.objects.order_by('-item_buying_date')[:5]
    context = {'latest_items_list': latest_items_list}
    return render(request, 'items/index.html', context) 

def detail(request, item_name):
    item = get_object_or_404(Stock, pk=item_name)
    return render(request, 'items/detail.html', {'item': item})

def results(request, item_id):
    response = "You're looking at the stock of items %s."
    return HttpResponse(response % item_id)

def vote(request, question_id):
    question = get_object_or_404(Stock, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Product.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))