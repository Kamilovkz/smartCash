from django.urls import path

from . import views

app_name = 'items'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<str:item_name>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:item_id>/results/', views.results, name='results'),
    # ex: /polls/5/choose/
    path('<int:item_id>/choose/', views.choose, name='choose'),
]