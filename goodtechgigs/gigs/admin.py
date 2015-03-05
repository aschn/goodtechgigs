from django.contrib import admin
from gigs.models import Gig

class GigAdmin(admin.ModelAdmin):
    list_display = ('id', 'poster', 'title', 'status')

admin.site.register(Gig, GigAdmin)
