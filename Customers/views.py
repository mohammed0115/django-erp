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
from .models import Customer
# from Products.forms import ProductForm


class ProductCreate(CreateView):
    model = Customer
    fields=['nationalno','fname','minName','lname','email','phone']
    success_url = reverse_lazy('customer-list')
  
class ProductUpdate(UpdateView):
    model = Customer
    fields=['nationalno','fname','minName','lname','email','phone']
    success_url = reverse_lazy('customer-list')

class ProductDelete(DeleteView):
    # form_class = ProductForm
    model= Customer
    success_url = reverse_lazy('customer-list')
    
class ProductDetailView(DetailView):
    model= Customer
    
class ProductListView(ListView):
    queryset= Customer.objects.all()