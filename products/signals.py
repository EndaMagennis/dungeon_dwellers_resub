from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import ProductImage


@receiver(post_save,sender=ProductImage)
def get_image_url(sender, instance, **kwargs):
    # Get the image url and save it to the instance
    instance.image_url = instance.image.url
    instance.save()


