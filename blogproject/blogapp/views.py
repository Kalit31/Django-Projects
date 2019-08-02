from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog


# Create your views here.

# def index(request):
#     blogs = Blog.objects.all()
#     if request == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return render(request, "index.html", {'blogs': blogs, 'user': user})
#     return render(request, "index.html", {'blogs': blogs, 'user': None})

def index(request):
    blogs = Blog.objects.all()
    if request.method == 'POST':
        usname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=usname, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, "index.html", {'blogs': blogs, 'user': user})
    return render(request, "index.html", {'blogs': blogs, 'user': None})


def user_logout(request):
    blogs = Blog.objects.all()
    logout(request)
    return render(request, "index.html", {'blogs': blogs, 'user': None})
