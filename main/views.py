from django.shortcuts import render
from django.views.generic import ListView
from main.models import Post
def index(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "index.html", {"posts": posts})

class IndexView (ListView):
    model = Post
    ordering = ["-created_at"]
    template_name = "index.html"
    context_object_name = "posts"