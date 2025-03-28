# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import FeedbackSerializer
from ..services import feedback_modifier

class SaveFeedbackView(APIView):
    def post(self, request, *args, **kwargs):
        modified_data = feedback_modifier(request.data)
        serializer = FeedbackSerializer(data=modified_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Feedback saved successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
