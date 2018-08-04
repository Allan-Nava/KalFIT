################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   04/08/2018
#   Aggiornamento   :   04/08/2018
#
#
#################################################################################
from django.conf.urls   import url
from frontend           import views
#
urlpatterns = [
    url(r'^$', views.home, name='home'),
]