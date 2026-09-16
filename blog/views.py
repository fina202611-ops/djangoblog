from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def home(request):
    return render(request, "blog/home.html", {"title": "Home"})


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def contact(request):
    return render(request, "blog/contact.html", {"title": "Contact"})


def base(request):
    return render(request, "blog/base.html", {"title": "Base"})


def post_list(request):
    posts = Post.objects.filter(status="published").order_by("-created_at")
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/post_list.html", {"page_obj": page_obj})