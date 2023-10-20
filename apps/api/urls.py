from django.urls import path, include
from .views import *

urlpatterns = [
    #plane
    path('plane/', Plane_views_list),
    path('plane/<int:pk>/', Plane_views_detail),

    #airline
    path('airline/', AirLine_views_list),
    path('airline/<int:pk>/', AirLine_views_detail),

    #flight
    path('flight/', Flight_views_list),
    path('flight/<int:pk>/', Flight_views_detail),

    path('auth/', include('dj_rest_auth.urls')),
    
]