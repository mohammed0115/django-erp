from django.urls import path
from .views import (ProductDetailView,ProductDelete,
ProductListView,ProductUpdate,ProductCreate,ProductUpdate)

urlpatterns = [
    #...
    path('customer/<int:pk>/', ProductDetailView.as_view(), name='customer-detail'),
    path('customer/', ProductListView.as_view(), name='customer-list'),
    path('customer/delete/<int:pk>', ProductDelete.as_view(), name='customer-delete'),
    path('customer/create/', ProductCreate.as_view(), name='customer-create'),
    path('customer/update/<int:pk>', ProductUpdate.as_view(), name='customer-update'),



]