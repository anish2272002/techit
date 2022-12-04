from django import forms
from .models import GalleryPhoto

class GalleryPhotoForm(forms.ModelForm):
    class Meta:
        model=GalleryPhoto
        fields=("file","caption")
        labels={
            "file":"",
            "caption":""
        }
        widgets={
            'file':forms.FileInput(attrs={
                'class':'form-control',
                'placeholder':'Image'
            }),
            'caption':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Caption'
            }),
        }