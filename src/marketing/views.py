from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
# from .forms import SubscriptionForm
from .models import Subscription
from GEL.utils import SendSubscribeMail

import json
import requests

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = 'https://{dc}.api.mailchimp.com/3.0'.format(dc=MAILCHIMP_DATA_CENTER)
members_endpoint = '{api_url}/lists/{list_id}/members'.format(
    api_url=api_url,
    list_id=MAILCHIMP_EMAIL_LIST_ID
)


# def subscribe(email):
#     data = {
#         "email_address": email,
#         "status": "subscribed"
#     }
#     r = requests.post(
#         members_endpoint,
#         auth=("", MAILCHIMP_API_KEY),
#         data=json.dumps(data)
#     )
#     return r.status_code, r.json()

# def subscribe(request):
#     if request.method == 'POST':
#         email = request.POST['email_id']
#         email_qs = Subscribe.objects.filter(email_id=email)
#         if email_qs.exists():
#             data = {"status": "404"}
#             return JsonResponse(data)
#         else:
#             Subscribe.objects.create(email_id=email)
#             # Send the Mail, Class available in utils.py
#             SendSubscribeMail(email)

#     return HttpResponse("/")


# def email_list_sign_up(request):
#     form = SubscriptionForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             email_signup_qs = Subscription.objects.filter(
#                 email=form.instance.email)
#             if email_signup_qs.exists():
#                 messages.info(request, "You are already subscribed")
#             else:
#                 subscribe(form.instance.email)
#                 form.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def subscribe_email(request):
    if request.method == 'GET':
        email = request.GET['email']

        subscribed_email = Subscription.objects.filter(email=email)
        if not subscribed_email.exists():
            subscription = Subscription(email=email)
            subscription.save()
    return HttpResponseRedirect(request.path_info)
