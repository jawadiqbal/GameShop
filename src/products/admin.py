from django.contrib import admin

# Register your models here.

from .models import Product

class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["title", "developer", "publisher", "quantity", "price"]
	search_fields = ["title", "developer", "publisher"]
	class Meta:
		model = Product

admin.site.register(Product, ProductModelAdmin)
# Product.objects.get(category__icontains="Action") to find action games
