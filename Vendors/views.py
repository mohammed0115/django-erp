from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy,reverse
# from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse
# from django.views.generic.edit import FormView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView,ListView
from .models import Vendor
# from Products.forms import ProductForm


class VendorCreate(CreateView):
    model = Vendor
    fields=['nationalno','fname','minName','lname','email','phone']
    success_url = reverse_lazy('Vendor-list')
  
class VendorUpdate(UpdateView):
    model = Vendor
    fields=['nationalno','fname','minName','lname','email','phone']
    success_url = reverse_lazy('Vendor-list')

class VendorDelete(DeleteView):
    # form_class = ProductForm
    model= Vendor
    success_url = reverse_lazy('Vendor-list')
    
class VendorDetailView(DetailView):
    model= Vendor
    
class VendorListView(ListView):
    queryset= Vendor.objects.all()