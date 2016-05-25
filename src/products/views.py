from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from .form_add_product import AddProductForm
from .form_add_product import CronForm
from .form_add_product import Rating

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

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(developer__icontains=query) |
                Q(publisher__icontains=query) |
                Q(category__icontains=query)
            ).distinct()
        filter_var = "q"

    paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
    page = (request.GET.get(filter_var))
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
        "title": "GameShop",
        "filter_var": filter_var,
        "page_request_var": page,
    }
    return render(request, "index.html", context)


@csrf_protect
def product_detail(request, slug=None):
    obj = get_object_or_404(Product, slug=slug)
    form = Rating(request.POST or None)
    if form.is_valid():
        instance = form.cleaned_data[ 'avg_rating' ]
        temp = form.cleaned_data[ 'users_rated' ]
        instance.save()
    context = {
        "object": obj,
        "title": obj.title,
    }
    return render(request, "detail.html", context)



def add_product(request):
    form = AddProductForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Added")
    context = {
        "form": form,
    }
    return render(request, "add_product.html", context)


def restock(request):
    form = CronForm(request.POST or None)
    if form.is_valid():
        instance = form.cleaned_data[ 'game' ]
        temp = form.cleaned_data[ 'add_keys' ]
        instance.add_keys = temp
        instance.save()
        messages.success(request, "Successfully Updated")
    context = {
        "form": form,
    }
    return render(request, "restock.html", context)

def staff(request):
    return render(request, "staff.html",{})

def profile(request):
    return render(request, "profile.html",{})

def about(request):
    return render(request, "about.html",{})

def contact(request):
    return render(request, "contact.html",{})

def buy_now(request, slug=None):
    #print "kutta"
    obj = get_object_or_404(Product, slug=slug)
    context = {
        "object": obj,
        "title": obj.title,
    }
    return render(request, "purchase.html", context)

def purchase(request, slug=None):
    obj = get_object_or_404(Product, slug=slug)
    return render(request, "done.html", {})

def done(request, slug=None):
    return render(request, "done.html", {})
