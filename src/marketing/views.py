from django.conf import settings
from django.http import HttpResponseRedirect
from .models import Subscription


def subscribe_email(request):
    if request.method == 'GET':
        email = request.GET['email']

        subscribed_email = Subscription.objects.filter(email=email)
        if not subscribed_email.exists():
            subscription = Subscription(email=email)
            subscription.save()
    return HttpResponseRedirect(request.path_info)
