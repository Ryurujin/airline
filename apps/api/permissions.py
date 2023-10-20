from rest_framework.permissions import BasePermission

#plane
class PlanePermission(BasePermission):
    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return request.user.is_staff
        
        elif request.method == 'POST':
            return request.user.is_authenticated
    
class PlaneDetailPermission(BasePermission):
    def has_permission(self, request, view):
        
        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_authenticated
        

#airline
class AirlinePermission(BasePermission):
    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True
        
        elif request.method == 'POST':
            return request.user.is_authenticated

class AirlineDetailPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated
        
        elif request.method == ['GET']:
            return True
        

#flight
class FlightPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'POST']:
            return request.user.is_authenticated


class FlightDetailPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_authenticated
        
        