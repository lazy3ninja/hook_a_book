from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseRedirect
# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        form = ProductForm()
        return render(request, "selling/saving.html")
    context = {
        'form' : form
    }
    return render(request, "selling/selling.html", context)

def product_detail_view(request):
    obj = Product.objects.get()
    context = {
        'object' : obj
    }
    return render(request, "selling/selling.html", context)