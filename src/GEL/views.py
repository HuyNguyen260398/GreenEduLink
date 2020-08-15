from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
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


def about(request):
    context = {}
    return render(request, "about.html", context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def send_email(request):
    context = {}

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        if name and email and message:
            subject = name + ' - ' + email
            body = message

            send_mail(subject, body, settings.EMAIL_HOST_USER, [
                settings.EMAIL_HOST_USER], fail_silently=False)

            context['success_msg'] = 'Thank you! Your message has been sent!'
        else:
            context['error_msg'] = 'Sorry! Your message is not valid!'

    return render(request, 'contact.html', context)


def founder_info(request):
    post_list = Post.objects.all().order_by('-created_at')[:3]
    tag_list = Tag.objects.all()

    context = {
        'post_list': post_list,
        'tag_list': tag_list,
    }
    return render(request, 'founder.html', context)
