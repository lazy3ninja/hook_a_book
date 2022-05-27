from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    product = Product.objects.all()
    return render(request, "buying/index.html", {
        'product' : product
    })