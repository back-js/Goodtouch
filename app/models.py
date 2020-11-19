
from django.db import models

class Image(models.Model):
    age = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='source' ,blank=True)
    image2 = models.ImageField(upload_to='reference' ,blank=True)

    def __str__(self):
        return self.age