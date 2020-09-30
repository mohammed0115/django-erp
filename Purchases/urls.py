from django.urls import path
from .views import index

urlpatterns = [
    
    path('Purchase/', index, name='purchase-index'),



]