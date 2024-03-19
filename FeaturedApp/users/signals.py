from django.db.models.signals import post_save #fired after user is saved
from django.contrib.auth.models import User #sender of the signal
from django.dispatch import receiver #receiver of the signal
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


#save profile when user is saved
@receiver(post_save, sender=User)
def create_profile(sender, instance,  **kwargs):
    instance.profile.save()