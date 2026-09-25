from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Category, Post  # Добавили Category


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status="published").order_by("-created_at")

    # 👇 Добавлено отсюда (Часть C)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(status="published")


def about(request):
    return render(request, "blog/about.html", {"team": "DjangoBlog Team"})


def contact(request):
    return render(request, "blog/contact.html")