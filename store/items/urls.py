from django.urls import path
from . import views
from items.scripts import reports as report
from items.scripts import instructions as instruction
from items.scripts import about as about

urlpatterns = [
    path('', views.index, name='index'),
    path('stock/', views.GlassesListView.as_view(), name='stock'),
    path('orders/', views.OrdersListView.as_view(), name='order'),
    path('addstock/', views.add_stock, name='add_stock'),
    path('addorder/', views.add_order, name='add_order'),
    path('about/', about.about, name='about'),
    path('instructions/', instruction.instructions, name='instructions'),
    path('reports/', report.reports, name='reports'),
    path('delete-item/<str:pk>/', views.delete_item, name='delete_item'),
    path('update-order/<str:pk>/', views.update_order, name='update-order'),
]