from django.db import models
import datetime

# Create your models here.


class Subscription(models.Model):
    email = models.EmailField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.email
