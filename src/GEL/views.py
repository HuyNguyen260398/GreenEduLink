from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
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
    context = {
        'response_msg': '',
    }

    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     email = request.POST.get('email', '')
    #     message = request.POST.get('message', '')

    #     if name and email and message:
    #         subject = name + ' - ' + email
    #         body = message

    #         try:
    #             send_mail(subject, body, settings.EMAIL_HOST_USER, [
    #                 settings.EMAIL_HOST_USER], fail_silently=False)
    #             return render(request, 'home.html', context)

    #         except BadHeaderError:
    #             # messages.error(
    #             #     request, 'Invalid header found')
    #             context['response_msg'] = 'Invalid header found'

    #         # messages.success(
    #         #     request, 'Your message has been sent. Thank you!')

    #         context['response_msg'] = 'Your message has been sent. Thank you!'
    #         # return render('contact.html', {'response_msg': 'Your message has been sent. Thank you!'})

    #         # return HttpResponseRedirect(request.path_info)
    #         # return render("contact.html", context)

    #     else:
    #         # messages.warning(
    #         #     request, 'Make sure all fields are entered and valid.')
    #         context['response_msg'] = 'Make sure all fields are entered and valid.'

    #     return render(request, 'home.html', context)

    return render(request, 'contact.html', context)


def send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        if name and email and message:
            subject = name + ' - ' + email
            body = message

            send_mail(subject, body, settings.EMAIL_HOST_USER, [
                settings.EMAIL_HOST_USER], fail_silently=False)

    return redirect('home')
