from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import GalleryItem

class GalleryIndexView(ListView):
    model=GalleryItem
    template_name="gallery.html"
    context_object_name = "GalleryItems"