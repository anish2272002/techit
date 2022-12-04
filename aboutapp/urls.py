from django.urls import path
from .views import ContactView,AboutView,FaqView

app_name="about"

urlpatterns = [
    path('',AboutView.as_view(),name="aboutus"),
    path('contact',ContactView.as_view(),name="contact"),
    path('faq',FaqView.as_view(),name="faq")
]