from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from notes.models import UserProfile, Membership, Note
import os.path

@receiver(post_save, sender=Note)
def model_post_change(sender, instance, created, **kwargs):
    if created:
        membership = Membership.objects.filter(user=instance.user).first()
        if membership.credits_left > 0:
            membership.credits_left -= 1
            membership.save()
        else:
            raise "No credits yo!!"


@receiver(post_save,sender=User)
def create_user_profile_post_user_creation(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        UserProfile.objects.create(user=user)



