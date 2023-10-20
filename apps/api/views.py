from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from .serializers import *
from apps.app.models import *

"""#ViewSet
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication"""


#plane 
class Plane_views_list(APIView):
    def get(self, request):
        planes = ModelsPlane.objects.all()
        serializer = PlaneSerializer(planes, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = PlaneSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Plane_views_detail(APIView):
    def get(self, request, pk):
        plane = ModelsPlane.objects.get(pk=pk)
        serializer = PlaneSerializer(plane)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        plane = ModelsPlane.objects.get(pk=pk)
        serializer = PlaneSerializer(plane, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        plane = ModelsPlane.objects.get(pk=pk)
        plane.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    


#airline 
class AirLine_views_list(APIView):
    def get(self, request):
        airlines = ModelsAirline.objects.all()
        serializer = AirLineSerializer(airlines, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = AirLineSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class AirLine_views_detail(APIView):
    def get(self, request, pk):
        airlines = ModelsAirline.objects.get(pk=pk)
        serializer = PlaneSerializer(airlines)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        airlines = ModelsAirline.objects.get(pk=pk)
        serializer = AirLineSerializer(airlines, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        airlines = ModelsAirline.objects.get(pk=pk)
        airlines.delete()
        return Response(status=HTTP_204_NO_CONTENT)


#flight                                                                                                                                            v                      
class Flight_views_list(APIView):
    def get(self, request):
        flights = ModelsFlight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = FlightSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Flight_views_detail(APIView):
    def get(self, request, pk):
        flights = ModelsFlight.objects.get(pk=pk)
        serializer = FlightSerializer(flights)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        flights = ModelsFlight.objects.get(pk=pk)
        serializer = FlightSerializer(flights, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        flights = ModelsFlight.objects.get(pk=pk)
        flights.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    


