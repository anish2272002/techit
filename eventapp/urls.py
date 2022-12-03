from django.urls import path
from .views import EventCreateView,EventListView,EventDetailView,EventDeleteView

app_name="event"

urlpatterns = [
    path('<int:isCompetition>',EventListView.as_view(),name="eventlist"),
    path('create/<int:isCompetition>',EventCreateView.as_view(),name="eventcreate"),
    path('detail/<int:pk>',EventDetailView.as_view(),name="eventdetail"),
    path('delete/<int:pk>',EventDeleteView.as_view(),name="eventdelete"),
]