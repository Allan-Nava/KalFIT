from django.http                            import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse, HttpResponseRedirect)
################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   29/05/2018
#   Aggiornamento   :   29/05/2018
#
#
#################################################################################
from django.http                            import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse, HttpResponseRedirect)
from django.shortcuts                       import render
#
# Create your views here.
def home(request):

    return HttpResponse('You\'re at the index. KALFIT')