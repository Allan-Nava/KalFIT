# -*- coding: utf-8 -*-
################################################################################
#
#   Autore          :   Allan Nava
#   Data            :   03/08/2018
#   Aggiornamento   :   04/08/2018
#
#
#################################################################################
#
from django.contrib         import admin
from django.db.models       import Q
from alimentation.models    import Alimentation
#
#
# Register your models here.
@admin.register(Alimentation)
class AlimentationAdmin(admin.ModelAdmin):
    pass
