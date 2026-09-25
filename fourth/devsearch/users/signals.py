from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User


# @receiver(post_save, sender=Profile)
def profile_updated(sender, instance, created, **kwargs):
    print("profile signal")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )

post_save.connect(profile_updated, sender=Profile)

# @receiver(post_delete, sender=Profile)
def profile_delete(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_delete.connect(profile_delete, sender=Profile)
