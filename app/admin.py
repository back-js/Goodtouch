from django.contrib import admin

from .models import Image

class ImageAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['age','country' ,'image1', 'image2']

admin.site.register(Image, ImageAdmin)