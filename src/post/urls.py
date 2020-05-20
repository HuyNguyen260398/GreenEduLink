from django.urls import path

from .views import (
    news,
)

app_name = 'post'

urlpatterns = [
    path('news/', news, name='news')
]