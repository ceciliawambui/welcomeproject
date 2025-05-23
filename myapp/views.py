from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Subscriber
from .forms import BlogForm
from django.contrib import messages 

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

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(display_blogs)
    else:
        form = BlogForm()
        return render(request, 'add_blog.html', {'form':form})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email = email).exists():
            messages.error(request, "You are already subscribed!")
        else:
            subscriber = Subscriber(email = email)
            subscriber.save()
            messages.success(request, "Thank you for subscribing!")
            return redirect(subscribe)
    return render(request, 'subscribe.html')
            
