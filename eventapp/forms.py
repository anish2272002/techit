from django import forms
from .models import EventModel

class EventCreateForm(forms.ModelForm):
    class Meta:
        model=EventModel
        fields=("eventType","title","startDateTime","description","body","picture","duration")
        labels={
            "eventType":"",
            "startDateTime":"Start Date Time",
            "duration":"Duration",
            "title":"",
            "description":"",
            "body":"",
            "picture":""
        }
        widgets={
            'eventType':forms.Select(attrs={
                'class':'form-select',
                'placeholder':'Type'
            }),
            'startDateTime':forms.DateTimeInput(format=('%j-%M-%Y %H-%i'),attrs={
                'type': 'datetime-local',
                'class':'form-control',
                'placeholder':'Start Date & Time'
            }),
            'duration':forms.NumberInput(attrs={
                'type':'range',
                'min':'0.5',
                'max':'48',
                'step':'0.5',
                'value':'1'
            }),
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title'
            }),
            'description':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Description',
                'rows':'2'
            }),
            'picture':forms.FileInput(attrs={
                'class':'form-control',
                'placeholder':'Image'
            }),
            'body':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Body',
                'rows':'10'
            }),
        }