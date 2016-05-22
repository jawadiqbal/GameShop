from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone

from django.utils.text import slugify

from django.db import models

import string
import random

# Create your models here.

def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s.%s" %(instance.slug, instance.slug, extension)

class Product(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField(upload_to=upload_location,null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    developer = models.CharField(max_length=120,null=True)
    publisher = models.CharField(max_length=120,null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    category = models.CharField(max_length=120,null=True)
    quantity = models.IntegerField(default=10)
    keys_size = models.IntegerField(default=0,null=True,blank=True)
    keys = models.CharField(max_length=1200,null=True,blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_price(self):
        return "$%s" % self.price

    def get_category_title(self):
        return self.category

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    prev_keys_size = instance.keys_size
    instance.keys_size = int(instance.quantity) * 5
    if instance.keys_size > prev_keys_size :
        add = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(instance.keys_size-prev_keys_size))
        instance.keys = instance.keys + add
    elif instance.keys_size < prev_keys_size :
        sub = prev_keys_size - instance.keys_size
        instance.keys = instance.keys[:-sub]

pre_save.connect(pre_save_post_receiver, sender=Product)
