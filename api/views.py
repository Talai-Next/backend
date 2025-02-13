from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LineOneRouteSerializer
from .models import LineOneRoute
class LineOneRouteViewSet(viewsets.ModelViewSet):
    queryset = LineOneRoute.objects.all().order_by('order')
    serializer_class = LineOneRouteSerializer

