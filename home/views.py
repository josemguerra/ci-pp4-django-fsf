from django.shortcuts import render
from blog.models import Post


def home_view(request):
    featured_post_list = Post.objects.filter(
        approved=True, featured=True, status="PB"
        )
    template = ["home/index.html"]
    context = {
        "featured_post_list": featured_post_list,
    }
    return render(request, template, context)
