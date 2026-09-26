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

def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created is False:
        user.first_name = profile.name
        user.user_name = profile.user_name
        user.email = profile.email
        user.save()

post_save.connect(update_user, sender=Profile)



