from django.contrib.admin import *
from .models import *

#aadmin  11

#plane
@register(ModelsPlane)
class PlaneAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

#airplane
@register(ModelsAirline)
class AirPlaneAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

#flight
@register(ModelsFlight)
class FlightAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

