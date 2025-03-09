from django.urls import include, path
from .views import BusStopLocationView, LineSpecailRouteView, LineOneRouteView, ObstacleMarkerView

urlpatterns = [
    path('line-one/', LineOneRouteView.as_view()),
    path('line-special/', LineSpecailRouteView.as_view()),
    path('bus-stop-location/', BusStopLocationView.as_view()),
    path('obstacle-marker/<str:obstacle_type>/', ObstacleMarkerView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

