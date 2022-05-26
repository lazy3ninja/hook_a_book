from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseRedirect
# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        img_object = form.instance
        form = ProductForm()
        return render(request, "selling/saving.html")
    img_object = form.instance
    context = {
        'form' : form,
        'imgobj' : img_object
    }
    return render(request, "selling/selling.html", context)

def product_detail_view(request):
    obj = Product.objects.get()
    context = {
        'object' : obj
    }
    return render(request, "selling/selling.html", context)