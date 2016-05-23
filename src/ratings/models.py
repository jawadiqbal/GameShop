from __future__ import unicode_literals

from django.db import models

from products.models import Product
from django.contrib.auth.models import User

from django.db.models.signals import pre_save

# Create your models here.

class Rating(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    score = models.IntegerField(default=0,null=False)

    class Meta:
        unique_together = ("product", "user")

def pre_save_rating_receiver(sender, instance, *args, **kwargs):
    instance.product.avg_rating = Rating.objects.filter(product__title=instance.product.title).aggregate(models.Avg('score')).values()[0]
    instance.product.users_rated += 1
    instance.product.save()

pre_save.connect(pre_save_rating_receiver, sender=Rating)
