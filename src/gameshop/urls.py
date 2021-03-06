"""gameshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from products.views import (
    product_home,
    product_detail,
    staff,
    add_product,
    restock,
    profile,
    about,
    contact,
    buy_now,
    purchase,
    )

urlpatterns = [
    url(r'^$', product_home),
    url(r'^admin/', admin.site.urls),
    url(r'^products/$', product_home),
    url(r'^products/(?P<slug>[\w-]+)/$', product_detail),
    url(r'^staff/$', staff),
    url(r'^staff/add_product/$', add_product),
    url(r'^staff/restock/$', restock),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', profile),
    url(r'^about/$', about),
    url(r'^contact/$', contact),
    url(r'^products/(?P<slug>[\w-]+)/purchase/$', buy_now),
    url(r'^products/(?P<slug>[\w-]+)/purchase/done/$', purchase),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
