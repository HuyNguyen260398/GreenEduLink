from django.shortcuts import render
from django.core.paginator import Paginator

from .models import *

# Create your views here.


def gallery(request):
    pictures = Picture.objects.all().order_by('-timestamp')
    picture_section = pictures[0]
    video_section = pictures[1]
    context = {
        'picture_gallery': picture_section,
        'video_gallery': video_section,
    }
    return render(request, 'gallery/gallery.html', context)


def picture_gallery(request):
    pictures = Picture.objects.all().order_by('-timestamp')
    paginator = Paginator(pictures, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'pictures': pictures,
        'page_obj': page_obj
    }
    return render(request, 'gallery/picture_gallery.html', context)


def video_gallery(request):
    videos = Video.objects.all().order_by('-timestamp')
    paginator = Paginator(videos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'videos': videos,
        'page_obj': page_obj
    }
    return render(request, 'gallery/video_gallery.html', context)
