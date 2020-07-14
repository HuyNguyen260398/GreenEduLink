from django import forms
from .models import Subscribe


# class SubscribeForm(forms.ModelForm):
#     email = forms.EmailField(widget=forms.TextInput(attrs={
#         "id": "mc-email",
#         "type": "email",
#         "name": "email",
#         "placeholder": "Enter your email address..."
#     }), label="")

#     class Meta:
#         model = Subscribe
#         fields = ('email', )
