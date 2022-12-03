from django.db import models

class EventModel(models.Model):
    id=models.BigAutoField(primary_key=True)
    eventType = models.CharField(max_length=256,choices=[('Hackathon','Hackathon'),('Workshop','Workshop'),('Competition','Competition')],default=('Competition','Competition'))
    startDateTime = models.DateTimeField()
    duration = models.IntegerField()
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    body = models.TextField(max_length=3840)
    picture = models.ImageField(upload_to='eventpic')
    def __str__(self):
        return "{0} : {1} : {2}".format(self.startDateTime,self.eventType,self.title)