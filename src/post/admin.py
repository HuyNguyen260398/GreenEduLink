from django.contrib import admin
from .models import (
    Post,
    Tag,
    PostTag,
)

class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    inlines = [PostTagInline]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)

admin.site.register(Tag)

admin.site.register(PostTag)
