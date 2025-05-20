from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def welcome(request):
    return HttpResponse("Welcome to our Django class!")

def home(request):
    context = {
        "message":"Welcome to my home page" 
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def display_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})
