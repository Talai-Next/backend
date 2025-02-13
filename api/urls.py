from django.urls import path
from .views import BusStopLocationView

urlpatterns = [
    path('bus-stop-location/', BusStopLocationView.as_view()),
]
