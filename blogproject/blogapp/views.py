from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog


# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    if request == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=username, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', {'blogs': blogs, 'user': None})

    return render(request, 'index.html', {'blogs': blogs, 'user': None})
