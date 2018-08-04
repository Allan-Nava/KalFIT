# -*- coding: utf-8 -*-
################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   04/08/2018
#   Aggiornamento   :   04/08/2018
#
#
#################################################################################
from django.http                            import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse, HttpResponseRedirect)
from django.shortcuts                       import render
#
# Create your views here.
def home(request):

    return render(request, 'landing/landing.html', )
    