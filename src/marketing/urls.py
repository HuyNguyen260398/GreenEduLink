from django.urls import path

from .views import *

app_name = 'marketing'

urlpatterns = [
    path('', subscribe_email, name='subscribe')
]
