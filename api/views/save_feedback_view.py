from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import FeedbackSerializer
from api.services import feedback_modifier
import logging

logger = logging.getLogger(__name__)

class SaveFeedbackView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            modified_data = feedback_modifier(request.data)
        except ValueError as e:
            logger.error(f"Error modifying feedback data: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FeedbackSerializer(data=modified_data)
        if serializer.is_valid():
            feedback_instance = serializer.save()
            logger.info(f"Feedback saved successfully: {feedback_instance}")
            return Response(FeedbackSerializer(feedback_instance).data, status=status.HTTP_201_CREATED)

        logger.error(f"Feedback validation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
