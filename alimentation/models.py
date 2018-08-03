################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   29/05/2018
#   Aggiornamento   :   02/08/2018
#
#
#################################################################################
from __future__ import unicode_literals
#
import hashlib, os.path, urllib, uuid
#
from django.conf                		import settings
from django.contrib.auth.models 		import User
from django.db                  		import models
from django.db.models.signals  	 		import post_save
from django.utils.encoding      		import python_2_unicode_compatible
from django.utils.translation                   import ugettext_lazy as _
from django.core.validators                     import RegexValidator
#
#
#
#
@python_2_unicode_compatible
class BaseAlimentation(models.Model):
	"""
	"""
	#
	name = models.CharField(max_length=150)
	code = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
	slug = models.SlugField(max_length=255)
	
	#
	class Meta:
		abstract = True

	#
#

