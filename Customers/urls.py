from django.urls import path
from .views import (CustomerDetailView,CustomerDelete,
CustomerListView,CustomerUpdate,CustomerCreate,CustomerUpdate)

urlpatterns = [
    #...
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customer/', CustomerListView.as_view(), name='customer-list'),
    path('customer/delete/<int:pk>', CustomerDelete.as_view(), name='customer-delete'),
    path('customer/create/', CustomerCreate.as_view(), name='customer-create'),
    path('customer/update/<int:pk>', CustomerUpdate.as_view(), name='customer-update'),



]