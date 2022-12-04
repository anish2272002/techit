from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse,reverse_lazy

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

from .models import EventModel
from .forms import EventCreateForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class EventCreateView(View):
    template_name = "eventcreate.html"
    @method_decorator(login_required)
    def get(self,request,isCompetition):
        return render(request,self.template_name,{'form':EventCreateForm(),'isCompetition':isCompetition})
    @method_decorator(login_required)
    def post(self,request,isCompetition):
        form=EventCreateForm(request.POST,request.FILES)
        if(form.is_valid()):
            obj=form.save(commit=False)
            obj.picture=form.cleaned_data['picture']
            obj.save()
            return HttpResponseRedirect(reverse("event:eventlist",kwargs={'isCompetition':isCompetition}))
        else:
            return render(request,self.template_name,{'form':form})

class EventListView(View):
    model=EventModel
    template_name = "eventlist.html"
    context_object_name = "eventlist"
    def get(self,request,isCompetition):
        if(isCompetition==1):
            objs=self.model.objects.filter(eventType='Competition')
        else:
            objs=self.model.objects.exclude(eventType='Competition')
        return render(request,self.template_name,{self.context_object_name:objs,'isCompetition':isCompetition})

class EventDetailView(DetailView):
    model=EventModel
    template_name="eventdetail.html"
    context_object_name="eventdetail"

class EventDeleteView(DeleteView):
    model=EventModel
    template_name="eventdelete.html"
    context_object_name="event"
    success_url=reverse_lazy("event:eventlist")
    @method_decorator(login_required)
    def get(self,request,pk):
        obj=self.model.objects.get(id=pk)
        return render(request,self.template_name,{self.context_object_name:obj})
    @method_decorator(login_required)
    def post(self,request,pk):
        event=get_object_or_404(self.model,id=pk)
        if(request.POST["event_title"]==event.title):
            isCompetition = 1 if(event.eventType=='Competition') else 0
            event.delete()
            return HttpResponseRedirect(reverse("event:eventlist",kwargs={'isCompetition':isCompetition}))
        else:
            return HttpResponseRedirect(reverse("event:eventdetail",kwargs={'pk':event.id}))