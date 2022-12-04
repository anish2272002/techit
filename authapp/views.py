from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.shortcuts import get_object_or_404

from .forms import LoginForm

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