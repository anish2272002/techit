from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import GalleryPhoto
from .form import GalleryPhotoForm
from django.http import HttpResponseRedirect
from django.urls import reverse

class GalleryIndexView(View):
    model=GalleryPhoto
    template_name="gallery.html"
    context_object_name = "GalleryPhotos"
    def get(self,request):
        return render(request,self.template_name,{'form':GalleryPhotoForm(),self.context_object_name:self.model.objects.all()})
    def post(self,request):
        form=GalleryPhotoForm(request.POST,request.FILES)
        if(form.is_valid()):
            obj=form.save(commit=False)
            obj.file=form.cleaned_data['file']
            obj.save()
            return HttpResponseRedirect(reverse("gallery:index"))
        else:
            return render(request,self.template_name,{'form':form,self.context_object_name:self.model.objects.all()})