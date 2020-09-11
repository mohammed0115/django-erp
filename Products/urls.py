from django.urls import path
from Products.views import (ProductDetailView,ProductDelete,
ProductListView,ProductUpdate,ProductCreate,ProductUpdate)

urlpatterns = [
    #...
    path('Product/<int:pk>/', ProductDetailView.as_view(), name='Product-detail'),
    path('Product/', ProductListView.as_view(), name='Product-list'),
    path('Product/delete/<int:pk>', ProductDelete.as_view(), name='Product-delete'),
    path('Product/create/', ProductCreate.as_view(), name='Product-create'),
    path('Product/update/<int:pk>', ProductUpdate.as_view(), name='Product-update'),



]