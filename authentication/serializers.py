################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   02/08/2018
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
from django.contrib.auth.models         import User
from django.db.models                   import Q
from django.contrib.auth                import authenticate, get_user_model
from django.utils.six                   import BytesIO
from django.utils.translation           import ugettext as _
#
from authentication.models             import Profile
#
# - Alimentation Serializer -
class ProfileSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model   = Profile
        fields  = ('__all__')
    #
#
class UserSerializer(serializers.ModelSerializer):
    #
    profile   = ProfileSerializer()
    #
    class Meta:
        model   = User
        fields  = ('id', 'first_name', 'last_name', 'email', 'username', 'profile', 'is_superuser', 'is_staff', 'last_login', 'date_joined', 'groups', 'user_permissions')
        #fields  = ('__all__')
    #
#