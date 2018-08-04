# -*- coding: utf-8 -*-
################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   29/05/2018
#   Aggiornamento   :   04/08/2018
#
#
#################################################################################
from __future__                                 import unicode_literals
#
import hashlib, os.path, urllib, uuid
#
from django.conf                		        import settings
from django.contrib.auth.models 		        import User
from django.db                  		        import models
from django.db.models.signals  	 		        import post_save
from django.utils.encoding      		        import python_2_unicode_compatible
from django.utils.translation                   import ugettext_lazy as _
from django.core.validators                     import RegexValidator
#
from alimentation.utils                         import OverwriteStorage
#
#
#
def upload_image(instance, filename):
    # file will be uploaded to MEDIA_ROOT/alimentation/alimentation<id>/<instance.name>
    fn, ext         = os.path.splitext(filename)
    new_filename    = instance.name + ext
    return 'alimentation/{0}/{1}'.format(instance.id, new_filename)
#
#
@python_2_unicode_compatible
class BaseObject(models.Model):
	"""This model represents the

    :Parameters:
      - `name`: (required)
      - `code`: (required)
      - `slug`: (required)
	"""
	#
	name = models.CharField(max_length=150)
	code = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
	slug = models.SlugField(max_length=255, blank=True, null=True)
	
	#
	class Meta:
		abstract = True

	#
#
@python_2_unicode_compatible
class Alimentation(BaseObject):
    """This model represents the

    :Parameters:
      - `description`: (not required)
      - `recipe`: (required)
      - `image`: (required)
      - `kcal`: (required)
      - `protein`: (required)
      - `satured_fat`: (required)
      - `unsatured_fat`: (required)
      - `sodium`: (required)
      - `satured`: (required)
	"""
    #
    no_image        = settings.MEDIA_URL +'alimentation/img.jpg'
    #
    description     = models.CharField(max_length=255, blank=True, null=True)
    recipe          = models.CharField(max_length=255)
    image           = models.ImageField(upload_to=upload_image, storage=OverwriteStorage(), default=no_image, null=True, blank=True)
    kcal            = models.IntegerField(default=0)
    protein         = models.IntegerField(default=0)
    satured_fat     = models.IntegerField(default=0)
    unsatured_fat   = models.IntegerField(default=0)
    sodium          = models.IntegerField(default=0)
    #
    class Meta:
        #
        db_table            = 'alimentation'
        verbose_name        = _('Alimentation')
        verbose_name_plural = _('Alimentations')
        #
    #
    def __unicode__(self):
        return self.name
    #
    def __str__(self):
        return self.name
    #
#
#
#