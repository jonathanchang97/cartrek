import requests

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User

from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_save, sender=User)
def get_profile_pic(sender, instance, **kwargs):
    try:
        url = instance.socialaccount_set.all()[0].get_avatar_url()
        pic = instance.get_username() + '.jpg'
        instance.profile.picture = pic
        with open('staticfiles/pics/' + pic, 'wb') as f:
            response = requests.get(url)
            f.write(response.content)
    except IndexError:
        # no facebook
        pass
