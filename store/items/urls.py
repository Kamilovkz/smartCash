from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stock/', views.GlassesListView.as_view(), name='stock'),
    path('orders/', views.OrdersListView.as_view(), name='order'),
    path('about/', views.about, name='about'),
    path('order/<int:pk>/', views.make_order, name='make_order'),
]