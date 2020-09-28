from django.shortcuts import render
from django.core.paginator import Paginator

from .models import *

# Create your views here.


def gallery(request):
    return render(request, 'gallery/gallery.html')


def picture_gallery(request):
    pictures = Picture.objects.all().order_by('-timestamp')
    context = {}
    if pictures.exists():
        paginator = Paginator(pictures, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['pictures'] = pictures
        context['page_obj'] = page_obj
    return render(request, 'gallery/picture_gallery.html', context)


def video_gallery(request):
    videos = Video.objects.all().order_by('-timestamp')
    context = {}
    if videos.exists():
        paginator = Paginator(videos, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['videos'] = videos,
        context['page_obj'] = page_obj
    return render(request, 'gallery/video_gallery.html', context)
