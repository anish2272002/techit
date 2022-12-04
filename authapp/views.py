from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.shortcuts import get_object_or_404

from .forms import LoginForm
from .models import UserProfile

class LoginView(View):
    form_class = LoginForm
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            usr=form.cleaned_data['user']
            login(request,usr)
            return HttpResponseRedirect(reverse('main:index'))
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('main:index'))

class AccountView(View):
    model=User
    template_name='account.html'
    context_object_name='account'
    def get(self,request,pk):
        return render(request,self.template_name,{self.context_object_name:self.model.objects.get(id=pk)})