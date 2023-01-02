from django.urls import path
from . import views

urlpatterns = [
    path('', views.GlassesListView.as_view(), name='index'),
    path('order/<int:pk>/', views.make_order, name='make_order'),
]