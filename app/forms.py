from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('source_image', 'reference_image')

        widgets = {
            'source_image': forms.ClearableFileInput(),
            'reference_image': forms.ClearableFileInput()
        }