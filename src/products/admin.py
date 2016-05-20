from django.contrib import admin

# Register your models here.

from .models import Product, Choice

class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["title", "developer", "publisher", "quantity", "price"]
	search_fields = ["title", "developer", "publisher"]
	class Meta:
		model = Product

admin.site.register(Product, ProductModelAdmin)
admin.site.register(Choice) # Product.objects.filter(category__title="Action") to find action games
