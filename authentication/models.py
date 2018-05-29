################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   29/05/2018
#   Aggiornamento   :   29/05/2018
#
#
#################################################################################
from __future__ import unicode_literals
#
import hashlib, os.path, urllib
#
from django.conf                import settings
from django.contrib.auth.models import User
from django.db                  import models
from django.db.models.signals   import post_save
from django.utils.encoding      import python_2_unicode_compatible
#
@python_2_unicode_compatible
class Profile(models.Model):
    """Profile extend User instance.

    :Parameters:
      - `user`:                         auth_user's username(required)
      - `location`:                     profile's first name (required)
      - `url`:                          profile's last name (required)
      - `job_title`:                    profile's job_title
      
    """
    user        = models.OneToOneField(User)
    location    = models.CharField(max_length=50, null=True, blank=True)
    url         = models.CharField(max_length=50, null=True, blank=True)
    job_title   = models.CharField(max_length=50, null=True, blank=True)
    #
    class Meta:
        db_table = 'auth_profile'
    #
    def __str__(self):
        return self.user.username
    #
#
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
#
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
#
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)