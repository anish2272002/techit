from django import forms
from .models import EventModel

class EventCreateForm(forms.ModelForm):
    class Meta:
        model=EventModel
        fields=("eventType","organizer","title","startDate","endDate","description","body","picture")
        labels={
            "eventType":"",
            "organizer":"",
            "startDate":"Start Date ",
            "endDate":"End Date ",
            "title":"",
            "description":"",
            "body":"",
            "picture":"Upload Poster "
        }
        widgets={
            'eventType':forms.Select(attrs={
                'class':'form-select',
                'placeholder':'Event Type'
            }),
            'organizer':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Event Organizer'
            }),
            'startDate':forms.DateInput(format=('%d-%m-%Y'),attrs={
                'type': 'date',
                'class':'form-control',
                'placeholder':'Start Date'
            }),
            'endDate':forms.DateInput(format=('%d-%m-%Y'),attrs={
                'type': 'date',
                'class':'form-control ',
                'placeholder': 'End Date'
            }),
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Event Title'
            }),
            'description':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Description'
            }),
            'picture':forms.FileInput(attrs={
                'class':'form-control',
                'placeholder':'Event Image'
            }),
            'body':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Event Body',
                'rows':'10'
            }),
        }