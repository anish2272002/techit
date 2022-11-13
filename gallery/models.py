from django.db import models

class GalleryItem(models.Model):
    id=models.BigAutoField(primary_key=True)
    type=models.CharField(max_length=256,choices=[('Photo','Photo'),('Video','Video')],default="Photo")
    content=models.FileField(upload_to='gallery')
    caption=models.CharField(max_length=256)