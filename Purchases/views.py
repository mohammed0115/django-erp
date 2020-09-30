from django.shortcuts import render

# Create your views here.
def index (request):
    context={
     "product":"product",
     "Invoice":"invoice"


    }
    return render(request,"Purchases/index.html",{})