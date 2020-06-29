from django.urls import path

from .views import *

app_name = 'gallery'

urlpatterns = [
    path('', gallery, name='gallery'),
    path('picture_gallery/', picture_gallery, name='picture_gallery'),
    path('video_gallery/', video_gallery, name='video_gallery'),
]
