from django.urls import path
from sales.views import index

urlpatterns = [
    
    path('sales/', index, name='sale-index'),



]