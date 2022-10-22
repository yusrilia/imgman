from django.db import models
from django.db.models.signals import pre_delete
import cloudinary
from cloudinary.models import CloudinaryField
from django.dispatch import receiver

# Create your models here.
class SinImg(models.Model):
    img = CloudinaryField('image', folder="media/images/single")

    def __str__(self):
        return f"#{self.id} {self.img.name.split('/')[-1]}"

@receiver(pre_delete, sender=SinImg)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.img.public_id)