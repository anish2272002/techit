from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=256,
        label='',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
    )
    password=forms.CharField(
        max_length=256,
        label='',
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
    )
    def clean(self):
        super().clean()
        usr=authenticate(username=self.cleaned_data['username'],password=self.cleaned_data['password'])
        if(usr):
            self.cleaned_data['user']=usr
        else:
            raise forms.ValidationError("Invalid Credentials")