from django import forms
from .models import Faq

class FaqForm(forms.ModelForm):
    class Meta:
        model=Faq
        fields=('question','answer')
        labels={
            'question':'',
            'answer':''
        }
        widgets={
            'question':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Question',
                'rows':'4'
            }),
            'answer':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Answer',
                'rows':'4'
            })
        }