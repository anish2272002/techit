from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse,reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from .models import EventModel

class EventListView(ListView):
    model=EventModel
    template_name = "eventlist.html"
    context_object_name = "eventlist"

class EventDetailView(DetailView):
    model=EventModel
    template_name="eventdetail.html"
    context_object_name="eventdetail"

class EventDeleteView(DeleteView):
    model=EventModel
    template_name="eventdelete.html"
    context_object_name="event"
    success_url=reverse_lazy("event:eventlist")
    def get(self,request,pk):
        return render(request,self.template_name,{self.context_object_name:self.model.objects.get(id=pk)})
    def post(self,request,pk):
        event=get_object_or_404(self.model,id=pk)
        if(request.POST["event_title"]==event.title):
            event.delete()
        return HttpResponseRedirect(reverse("event:eventlist"))