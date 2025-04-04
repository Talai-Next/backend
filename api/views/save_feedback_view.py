# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import FeedbackSerializer
from ..services import feedback_modifier

class SaveFeedbackView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            modified_data = feedback_modifier(request.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FeedbackSerializer(data=modified_data)
        if serializer.is_valid():
            feedback_instance = serializer.save()
            return Response(FeedbackSerializer(feedback_instance).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
