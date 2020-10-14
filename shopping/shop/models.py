from django.db import models
from django.utils.text import slugify
import uuid
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 264)
    slug = models.SlugField(allow_unicode = True,unique = True)
    catogory = models.CharField(max_length = 100,default = "")
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        return super().save(*args,**kwargs)

class Order(models.Model):
    finised = models.BooleanField(default = False)
    items = models.ManyToManyField(Item, through='OrderItem',related_name='orders')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='order_item', on_delete=models.CASCADE)
    quantity = models.IntegerField()