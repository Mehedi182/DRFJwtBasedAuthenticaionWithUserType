from django.contrib import admin
from .models import PartyUser

class PartyUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'type')


admin.site.register(PartyUser, PartyUserAdmin)
