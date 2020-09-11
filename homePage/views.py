from django.shortcuts import render

from django.template import Context, loader
# Create your views here.
def index (request):
    # template = loader.get_template("Base/home.html")
    # return   HttpResponse(template.render())
     return render(request,'Base/home.html',{})