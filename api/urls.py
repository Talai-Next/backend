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
    BusRouteView
)

urlpatterns = [
    path('line-one/', LineOneRouteView.as_view()),
    path('line-special/', LineSpecialRouteView.as_view()),
    path('line-three/', LineThreeRouteView.as_view()),
    path('line-five/', LineFiveRouteView.as_view()),
    path('bus-stop-location/', BusStopLocationView.as_view()),
    path('search/search-nearby-station/', SearchNearbyStationView.as_view()),
    path('search/available-line/', AvailableLineView.as_view()),
    path('search/available-station/', AvailableStationView.as_view()),
    path('search/bus-route', BusRouteView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

