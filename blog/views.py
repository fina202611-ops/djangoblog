from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})

def base(request):
    return render(request, 'blog/base.html', {'title': 'Base'})