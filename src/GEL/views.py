from django.shortcuts import render

from marketing.forms import SubscriptionForm


def home(request):
    form = SubscriptionForm()
    context = {
        'form': form
    }
    return render(request, "home.html", context)
