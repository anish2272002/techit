from select import select
from django.db import models
from django.forms import ImageField

class EventModel(models.Model):
    id=models.BigAutoField(primary_key=True)
    eventType = models.CharField(max_length=256,choices=[('Hackathon','Hackathon'),('Workshop','Workshop'),('Competition','Competition')])
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    organizer = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    body = models.TextField(max_length=256)
    picture = models.ImageField(upload_to='eventpic',default="../media/eventpic/icon-0.jpg",blank=True)
    def __str__(self):
        return "{0} : {1} : {2}".format(self.startDateTime,self.eventType,self.title)