from django.contrib import admin

# Register your models here.

from .models import Product

class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["title", "keys", "quantity", "price"]
	search_fields = ["title", "developer", "publisher"]
	class Meta:
		model = Product

admin.site.register(Product, ProductModelAdmin)

# Product.objects.get(category__icontains="Action") to find action games

# use foo[-N:] to get last N characters. key length is 5 so should use N = 5
# update quantity after that
