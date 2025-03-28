from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from ..serializers import LineSpecialRouteSerializer
from ..models import LineSpecialRoute



class LineSpecialRouteView(generics.ListAPIView):
    serializer_class = LineSpecialRouteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = LineSpecialRoute.objects.all().order_by('order')
        return bus_location