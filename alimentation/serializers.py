################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   04/08/2018
#   Aggiornamento   :   04/08/2018
#
#
#################################################################################
#
import uuid, warnings, json, requests
#
from datetime                           import datetime
from rest_framework                     import serializers, status
from rest_framework.parsers             import JSONParser
from rest_framework.response            import Response
#
from django.db                          import models
from django.db.models                   import Q
from django.contrib.auth                import authenticate, get_user_model
from django.utils.six                   import BytesIO
from django.utils.translation           import ugettext as _
#
from alimentation.models                import *
#
# - Alimentation Serializer -
class AlimentationSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model   = Alimentation
        fields  = ('__all__')
    #
#