from django.contrib import admin
from profiles.models import GigSeeker, GigPoster

class GigSeekerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'location')

class GigPosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'org_name', 'location')


admin.site.register(GigSeeker, GigSeekerAdmin)
admin.site.register(GigPoster, GigPosterAdmin)
