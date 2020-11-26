from django.contrib import admin

from .models import Image

class ImageAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['source_image', 'reference_image']

admin.site.register(Image, ImageAdmin)