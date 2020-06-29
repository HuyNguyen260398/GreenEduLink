from django.shortcuts import render

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
    context = {
        'pictures': pictures,
    }
    return render(request, 'gallery/picture_gallery.html', context)


def video_gallery(request):
    videos = Video.objects.all().order_by('-timestamp')
    context = {
        'videos': videos,
    }
    return render(request, 'gallery/video_gallery.html', context)
