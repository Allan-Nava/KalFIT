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
