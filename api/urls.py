from django.urls import include, path

from .views import BusStopLocationView, \
    LineSpecailRouteView, \
    LineOneRouteView, \
    LineFiveRouteView, \
    LineThreeRouteView, \
    SearchNearbyStationView, \
    AvailableLineView


urlpatterns = [
    path('line-one/', LineOneRouteView.as_view()),
    path('line-special/', LineSpecailRouteView.as_view()),
    path('line-three/', LineThreeRouteView.as_view()),
    path('line-five/', LineFiveRouteView.as_view()),
    path('bus-stop-location/', BusStopLocationView.as_view()),
    path('search-nearby-station/', SearchNearbyStationView.as_view()),
    path('available-line/', AvailableLineView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

