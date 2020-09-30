from django.urls import path
from .views import (VendorDetailView,VendorDelete,
VendorListView,VendorUpdate,VendorCreate,VendorUpdate)

urlpatterns = [
    #Vendor
    path('Vendor/<int:pk>/', VendorDetailView.as_view(), name='Vendor-detail'),
    path('Vendor/', VendorListView.as_view(), name='Vendor-list'),
    path('Vendor/delete/<int:pk>', VendorDelete.as_view(), name='Vendor-delete'),
    path('Vendor/create/', VendorCreate.as_view(), name='Vendor-create'),
    path('Vendor/update/<int:pk>', VendorUpdate.as_view(), name='Vendor-update'),



]