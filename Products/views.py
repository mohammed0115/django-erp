from django.shortcuts import render
from django.urls import reverse_lazy,reverse
# from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView,ListView
from Products.models import Product
from Products.forms import ProductForm


class ProductCreate(CreateView):
    form_class = ProductForm
    template_name="Products/product_create.html"
    success_url = '/'
    def form_valid(self, form):
        
       
        form.save()
        return super(ProductCreate, self).form_valid(form)

    def form_invalid(self, form):
        # print "form is invalid"
        return HttpResponse("form is invalid.. this is just an HttpResponse object")


    def get_success_url(self):
        return reverse("Product-list")

    def get_context_data(self, **kwargs):
        kwargs["object_list"] = Product.objects.all()
        return super(ProductCreate, self).get_context_data(**kwargs)

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse("Product-list")
    
    

class ProductDelete(DeleteView):
    # form_class = ProductForm
    model= Product
    success_url = reverse_lazy('Product-list')
    items_to_delete = []
   




class ProductDetailView(DetailView):
    model= Product
class ProductListView(ListView):
    queryset= Product.objects.all()