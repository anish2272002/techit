from django.db import models

class Faq(models.Model):
    id=models.BigAutoField(primary_key=True)
    question=models.CharField(max_length=356)
    answer=models.CharField(max_length=356)
    def __str__(self):
        return "FAQ {0} {1}".format(self.id,self.question[:15])