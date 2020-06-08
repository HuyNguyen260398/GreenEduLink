from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Picture

# Register your models here.


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    readonly_fields = ['image_load']

    def image_load(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        ))


# admin.site.register(Picture)
