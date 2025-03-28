from django.urls import include, path
from .views import (
    BusStopLocationView,
    LineSpecialRouteView,
    LineOneRouteView,
    LineFiveRouteView,
    LineThreeRouteView,
    SearchNearbyStationView,
    AvailableLineView,
    AvailableStationView,
    BusRouteView,
    ObstacleMarkerView, 
    proxy_buses,
    BusDataListView,
    LiveBusDataView
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  
    path('line-one/', LineOneRouteView.as_view()),
    path('line-special/', LineSpecialRouteView.as_view()),
    path('line-three/', LineThreeRouteView.as_view()),
    path('line-five/', LineFiveRouteView.as_view()),
    path('bus-stop-location/', BusStopLocationView.as_view()),  
    path('search/search-nearby-station/', SearchNearbyStationView.as_view()),
    path('search/available-line/', AvailableLineView.as_view()),
    path('search/available-station/', AvailableStationView.as_view()),
    path('search/bus-route', BusRouteView.as_view()),
    path('obstacle-marker/<str:obstacle_type>/', ObstacleMarkerView.as_view()),
    path('buses/', proxy_buses),
  
    path('bus-data/', BusDataListView.as_view()),
    path('live-bus-data/', LiveBusDataView.as_view(), name='live-bus-data')
]
