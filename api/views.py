from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LineOneRouteSerializer, LineSpecailRouteSerializer
from .models import LineOneRoute, LineSpecialRoute

class LineOneRouteViewSet(viewsets.ModelViewSet):
    queryset = LineOneRoute.objects.all().order_by('order')
    serializer_class = LineOneRouteSerializer

class LineSpecailRouteViewSet(viewsets.ModelViewSet):
    queryset = LineSpecialRoute.objects.all().order_by('order')
    serializer_class = LineSpecailRouteSerializer