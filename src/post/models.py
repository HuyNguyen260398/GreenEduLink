from django.db import models
from django.conf import settings
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # content = RichTextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=False)

