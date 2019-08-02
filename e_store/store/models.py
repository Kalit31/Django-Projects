from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.TextField()
    imglink = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    payment_data = models.CharField(max_length=100)
    items = models.TextField()
    fulfilled = models.BooleanField()
