from rest_framework.serializers import *
from apps.app.models import *

#plane
class PlaneSerializer(ModelSerializer):
    class Meta:
        model = ModelsPlane
        fields = '__all__'

#airline
class AirLineSerializer(ModelSerializer):
    class Meta:
        model = ModelsAirline
        fields = '__all__'

#flight
class FlightSerializer(ModelSerializer):
    class Meta:
        model = ModelsFlight
        fields = '__all__' 






        