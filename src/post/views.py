from django.shortcuts import render
from .models import *

def post(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "post/post.html", context)

def post_detail(request, id, slug):
    post = Post.objects.get(pk=id)
    post_list = Post.objects.exclude(pk=id)
    post_tag = PostTag.objects.filter(post_id=post)
    tag_list = Tag.objects.all()
    context = {
        'post': post,
        'post_list': post_list,
        'post_tag': post_tag,
        'tag_list': tag_list,
    }
    post.views += 1
    post.save()
    return render(request, 'post/post_detail.html', context)