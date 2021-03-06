from django.urls import path

from .views import *

app_name = 'post'

urlpatterns = [
    path('', post, name='post'),
    path('<int:id>/<slug:slug>/', post_detail, name='post_detail'),
    path('search/', post_search, name='post_search'),
    path('search_tag/<slug:tag>/', post_tag_search, name='post_tag_search'),
]
