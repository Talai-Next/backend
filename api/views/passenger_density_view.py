# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import FeedbackSerializer
from ..services import feedback_modifier

class DensityView(APIView):
    pass
