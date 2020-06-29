from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "id": "mc-email",
        "type": "email",
        "name": "email",
        "placeholder": "Enter your email address..."
    }), label="")

    class Meta:
        model = Subscription
        fields = ('email', )
