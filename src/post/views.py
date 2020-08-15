from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *
from .forms import CommentForm


def post(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'page_obj': page_obj
    }

    return render(request, "post/post.html", context)


def post_detail(request, id, slug):
    post = Post.objects.get(pk=id)
    post_list = Post.objects.exclude(pk=id).order_by('-created_at')[:5]
    post_tag = PostTag.objects.filter(post_id=post)
    tag_list = Tag.objects.all()
    comments = Comment.objects.filter(post=post).order_by('-created_on')
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'post_list': post_list,
        'post_tag': post_tag,
        'tag_list': tag_list,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }

    post.comments = comments.count()
    post.views += 1
    post.save()

    return render(request, 'post/post_detail.html', context)


def post_search(request):
    posts_qs = Post.objects.none()
    posts_tags_qs = PostTag.objects.none()
    list_post_id = []

    if request.method == 'GET':
        search_query = request.GET.get('search_query')
        if search_query != '' and search_query is not None:
            posts_tags_qs = PostTag.objects.filter(
                tag_id__name__icontains=search_query)

            if posts_tags_qs.exists():
                for post_tag in posts_tags_qs:
                    post = Post.objects.filter(id=post_tag.post_id.id).get()
                    list_post_id.append(post.id)

            posts_qs = Post.objects.filter(Q(title__icontains=search_query) |
                                           Q(id__in=list_post_id) |
                                           Q(description__icontains=search_query)).distinct().order_by('-created_at')
    paginator = Paginator(posts_qs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts_qs': posts_qs,
        'page_obj': page_obj,
        'search_query': search_query,
    }

    return render(request, "post/post.html", context)


def post_tag_search(request, tag):
    posts_qs = Post.objects.none()
    posts_tags_qs = PostTag.objects.none()
    list_post_id = []

    posts_tags_qs = PostTag.objects.filter(
        tag_id__name__icontains=tag)

    if posts_tags_qs.exists():
        for post_tag in posts_tags_qs:
            post = Post.objects.filter(id=post_tag.post_id.id).get()
            list_post_id.append(post.id)

    posts_qs = Post.objects.filter(
        Q(id__in=list_post_id)).distinct().order_by('-created_at')

    paginator = Paginator(posts_qs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts_qs': posts_qs,
        'page_obj': page_obj,
        'tag': tag,
    }

    return render(request, "post/post.html", context)
