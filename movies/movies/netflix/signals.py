from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
#from ./users import api_signup


@receiver(post_save,sender=User)
def user_created(sender, instance, created, *args, **kwargs):
    user = instance
    if created:  
        print('created user',instance.email)       
        send_mail(
            'Welcome to Netflix',
            "congratulations! You had successful Registration",
            'notifier.django@gmail.com',
            [instance.email],
            fail_silently=False
        )