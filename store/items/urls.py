from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stock/', views.GlassesListView.as_view(), name='stock'),
    path('orders/', views.OrdersListView.as_view(), name='order'),
    path('about/', views.about, name='about'),
    path('addStock/', views.add_stock, name='add_stock'),
    path('addOrder', views.add_order, name='add_order'),
    path('order/<int:pk>/', views.make_order, name='make_order'),
]