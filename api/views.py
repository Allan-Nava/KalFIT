# -*- coding: utf-8 -*-
################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   04/08/2018
#   Aggiornamento   :   04/08/2018
#
#
#################################################################################
#
import json
from datetime                           import datetime
from pprint                             import pprint
#
from rest_framework                     import viewsets, generics, status, mixins
from rest_framework.permissions         import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework.parsers             import JSONParser, FormParser, MultiPartParser
from rest_framework.response            import Response
from rest_framework.decorators          import api_view, detail_route, permission_classes, authentication_classes
from rest_framework.renderers           import JSONRenderer, TemplateHTMLRenderer, BrowsableAPIRenderer
from rest_framework.views               import APIView
#
from django.shortcuts                   import render
from django.conf                        import settings
from django.db                          import models
from django.contrib.auth.models         import User
#
from alimentation.models                 import Alimentation
from alimentation.serializers           import AlimentationSerializer
from authentication.serializers         import UserSerializer
#
#
# Create your views here.
class AlimentationViewSet(viewsets.ModelViewSet):
    """
    This viewset provides

    """
    #
    queryset            = Alimentation.objects.all()
    serializer_class    = AlimentationSerializer
    #
#
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset provides

    """
    #
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    #
#