from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
