from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from .models import Railways
from .models import LuasStops

admin.site.register(Railways, admin.GeoModelAdmin)
admin.site.register(LuasStops, admin.GeoModelAdmin)
