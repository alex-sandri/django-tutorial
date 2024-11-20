from django.contrib import admin

from .models import Lega, Specialità, Sport, Squadra

admin.site.register([Lega, Specialità, Sport, Squadra])
