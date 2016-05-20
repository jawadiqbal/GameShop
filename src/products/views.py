from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product

def product_home(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset,
        "title": "Game shop"
    }
    return render(request, "index.html", context)
