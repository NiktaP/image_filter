from django.db import models

# Create your models here.
class ImagesModels(models.Model):
    image=models.ImageField(upload_to='images/')
    new_image=models.ImageField(upload_to='images/processd/',null=True,blank=True)

    def __str__(self):
        return self.image.name


