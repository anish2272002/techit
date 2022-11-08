from django.shortcuts import render
from django.views.generic import View
from eventapp.models import EventModel

class IndexView(View):
    def get(self,request):
        return render(request,'index.html',{'eventlist':EventModel.objects.order_by('-id')[:5]})