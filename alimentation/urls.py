################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   29/05/2018
#   Aggiornamento   :   29/05/2018
#
#
#################################################################################
from django.conf.urls   import url
from alimentation       import views
#
urlpatterns = [
    url(r'^$', views.home, name='home'),
]