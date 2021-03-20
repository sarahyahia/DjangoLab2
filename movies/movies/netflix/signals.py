from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
#from ./users import api_signup


@receiver(post_save)
def user_created(sender, instance, created, *args, **kwargs):
    user = instance
    if created:         
        email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user=user)
        if email_is_created:
            short_hash = hashlib.sha1(str(random.random())).hexdigest()[:5]
            base, domain = str(user.email).split("@")
            activation_key = hashlib.sha1(short_hash+base).hexdigest()
            email_confirmed.activation_key = activation_key
            email_confirmed.save()
            email_confirmed.activate_user_email()

#user_logged_in.connect(get_create_stripe)
post_save.connect(user_created, sender=settings.AUTH_USER_MODEL)