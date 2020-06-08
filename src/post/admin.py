from django.contrib import admin
from django.utils.safestring import mark_safe

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
    readonly_fields = ['thumbnail_load']
    fields = (
        'user_id',
        'title',
        'description',
        'slug',
        'thumbnail',
        'thumbnail_load',
        'content',
        # 'created_at',
        'published_at',
        'updated_at',
        'views',
        'comments',
    )
    inlines = [PostTagInline]

    def thumbnail_load(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.thumbnail.url,
            width=obj.thumbnail.width,
            height=obj.thumbnail.height,
        ))

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)

admin.site.register(Tag)

admin.site.register(PostTag)
