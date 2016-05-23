from django.contrib import admin

# Register your models here.

from .models import Rating

class RatingModelAdmin(admin.ModelAdmin):
	list_display = ["product", "user", "score"]
	search_fields = ["product", "user", "score"]
	class Meta:
		model = Rating

admin.site.register(Rating, RatingModelAdmin)

# >>> from ratings.models import Rating
# >>> from django.db.models import Avg
# >>> Rating.objects.filter(product__title='Counter-Strike: Global Offensive').aggregate(Avg('score'))
