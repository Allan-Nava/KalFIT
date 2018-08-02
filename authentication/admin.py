################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   29/05/2018
#   Aggiornamento   :   29/05/2018
#
#
#################################################################################
from django.contrib         import admin
from django.db.models       import Q
from authentication.models  import Profile
#
#
#
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
