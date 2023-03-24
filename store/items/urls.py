from django.urls import path
from . import views
from items.scripts import reports as report
from items.scripts import instructions as instruction
from items.scripts import about as about
from items.scripts import index as index
from items.scripts import order as orders
from items.scripts import stock as stocks

urlpatterns = [
    
    path('', index.index, name='index'),
    path('about/', about.about, name='about'),
    path('instructions/', instruction.instructions, name='instructions'),
    path('reports/', report.reports, name='reports'),
    
    #Orders
    path('orders/', orders.OrdersListView.as_view(), name='order'),
    path('addorder/', orders.add_order, name='add_order'),
    path('update-order/<str:pk>/', orders.update_order, name='update-order'),
    
    #Stocks
    path('stock/', stocks.GlassesListView.as_view(), name='stock'),
    path('addstock/', stocks.add_stock, name='add_stock'),
    path('delete-item/<str:pk>/', stocks.delete_stock_item, name='delete_stock_item'),

]