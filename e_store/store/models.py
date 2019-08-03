from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=850)
    price = models.FloatField()
    desc = models.TextField()
    imglink = models.CharField(max_length=2000)


class Order(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=400)
    payment_method = models.CharField(max_length=400)
    payment_data = models.CharField(max_length=400)
    fulfilled = models.BooleanField()
    items = models.TextField()
