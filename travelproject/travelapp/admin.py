from django.contrib import admin
from . models import meet_team
from . models import place
# Register your models here.

admin.site.register(place)
admin.site.register(meet_team)