from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from mailjet_rest import Client
import os

class ContactView(View):
    def get(self,request):
        return HttpResponseRedirect(reverse("main:index")+"#contact")
    def post(self,request):
        api_key = os.environ['api_key']
        api_secret = os.environ['api_secret']
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
        'Messages': [
                {
                    "From": {
                        "Email": os.environ["senders_email"],
                        "Name": request.POST["contactfullname"]
                    },
                    "To": [
                        {
                            "Email": os.environ["receivers_email"],
                            "Name": "TechIT Helpdesk"
                        }
                    ],
                    "TemplateID": 4088499,
                    "TemplateLanguage": True,
                    "Subject": request.POST["contactsubject"],
                    "Variables": {
                        "Name": request.POST["contactfullname"],
                        "email": request.POST["contactemail"],
                        "body": "<br>".join(request.POST["contactmessage"].split('\n')),
                        "subject":request.POST["contactsubject"]
                    }
                }
            ]
        }
        result = mailjet.send.create(data=data)
        data = {
        'Messages': [
                {
                    "From": {
                        "Email": "anish2272002@gmail.com",
                        "Name": "TechIT"
                    },
                    "To": [
                        {
                            "Email": request.POST["contactemail"],
                            "Name": request.POST["contactfullname"]
                        }
                    ],
                    "TemplateID": 4088558,
                    "TemplateLanguage": True,
                    "Subject": "Acknowledgement: "+request.POST["contactsubject"],
                    "Variables": {
                        "Name": request.POST["contactfullname"]
                    }
                }
            ]
        }
        result = mailjet.send.create(data=data)
        return HttpResponseRedirect(reverse("main:index"))

class AboutView(View):
    def get(self,request):
        return render(request,"about.html",{})