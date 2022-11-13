from django.urls import path
from .views import GalleryIndexView
app_name="gallery"

urlpatterns = [
    path('',GalleryIndexView.as_view(),name="index"),
]