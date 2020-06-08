from django.shortcuts import render

from .models import *

# Create your views here.


def gallery(request):
    pictures = Picture.objects.all()
    context = {
        'pictures': pictures
    }
    return render(request, 'gallery/gallery.html', context)
