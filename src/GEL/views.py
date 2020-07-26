from django.shortcuts import render
from post.models import *


def home(request):
    posts = Post.objects.all().order_by('-created_at')[:4]
    university_posts = PostTag.objects.filter(
        tag_id__name='University').order_by('-post_id__created_at')[:3]
    context = {
        'posts': posts,
        'university_posts': university_posts
    }
    return render(request, "home.html", context)
