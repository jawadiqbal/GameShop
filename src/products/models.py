from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify

from django.db import models

# Create your models here.

def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s.%s" %(instance.slug, instance.slug, extension)

class Choice(models.Model):
    CATEGORY_OPTIONS = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Casual', 'Casual'),
        ('FPS', 'FPS'),
        ('Indie', 'Indie'),
        ('Multiplayer', 'Multiplayer'),
        ('RPG', 'RPG'),
        ('Racing', 'Racing'),
        ('Simulation', 'Simulation'),
        ('Sports', 'Sports'),
        ('Strategy', 'Strategy'),
    )
    title = models.CharField(max_length=120,choices=CATEGORY_OPTIONS)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField(upload_to=upload_location,null=True,blank=True)
    slug = models.SlugField(unique=True)
    developer = models.CharField(max_length=120,null=True)
    publisher = models.CharField(max_length=120,null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    category = models.ManyToManyField(Choice)
    quantity = models.IntegerField(default=10)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_price(self):
        return "$%s" % self.price

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Product)
