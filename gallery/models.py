from django.db import models

class GalleryPhoto(models.Model):
    id=models.BigAutoField(primary_key=True)
    file=models.ImageField(upload_to="gallery")
    caption=models.CharField(max_length=256)
    def __str__(self):
        return "{0} {1} {2}".format("Photo",self.id,self.caption)