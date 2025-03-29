from django.urls import include, path
from .views import *

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
    path('search/bus-route/', BusRouteView.as_view()),
    path('obstacle-marker/<str:obstacle_type>/', ObstacleMarkerView.as_view()),
    path('mockup-bus-data/', MockupBusesLocationListView.as_view()),
    path('live-bus-data/', PredictedBusDataView.as_view()),
    path('density-data/', DensityView.as_view()),

    path('receive-feedback/',SaveFeedbackView.as_view()),
]
