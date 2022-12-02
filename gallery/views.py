from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import GalleryPhoto

class GalleryIndexView(ListView):
    model=GalleryPhoto
    template_name="gallery.html"
    context_object_name = "GalleryPhotos"