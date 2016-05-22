from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Product

def product_home(request):
    filter_var = "all"
    queryset_list = Product.objects.all()
    if (request.GET.get('action')):
        queryset_list = Product.objects.filter(category__icontains="action")
        filter_var = "action"
    elif (request.GET.get('adventure')):
        queryset_list = Product.objects.filter(category__icontains="adventure")
        filter_var = "adventure"
    elif (request.GET.get('arcade')):
        queryset_list = Product.objects.filter(category__icontains="arcade")
        filter_var = "arcade"
    elif (request.GET.get('indie')):
        queryset_list = Product.objects.filter(category__icontains="indie")
        filter_var = "indie"
    elif (request.GET.get('multiplayer')):
        queryset_list = Product.objects.filter(category__icontains="multiplayer")
        filter_var = "multiplayer"
    elif (request.GET.get('racing')):
        queryset_list = Product.objects.filter(category__icontains="racing")
        filter_var = "racing"
    elif (request.GET.get('rpg')):
        queryset_list = Product.objects.filter(category__icontains="rpg")
        filter_var = "rpg"
    elif (request.GET.get('simulation')):
        queryset_list = Product.objects.filter(category__icontains="simulation")
        filter_var = "simulation"
    elif (request.GET.get('sports')):
        queryset_list = Product.objects.filter(category__icontains="sports")
        filter_var = "sports"
    elif (request.GET.get('strategy')):
        queryset_list = Product.objects.filter(category__icontains="strategy")
        filter_var = "strategy"


    paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
    page_request_var = "page"
    page = (request.GET.get(page_request_var))
    #print page
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "Game shop",
        "filter_var": filter_var,
        "page_request_var": page,
    }
    return render(request, "index.html", context)
