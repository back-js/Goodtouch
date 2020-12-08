
from django.db import models

class Image(models.Model):
    source_image = models.ImageField(upload_to='source' ,blank=True)
    reference_image = models.ImageField(upload_to='reference' ,blank=True)

    #def __str__(self):
    #    return self.source_image

