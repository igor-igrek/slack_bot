from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import parse_message


class Events(APIView):
    def post(self, request, *args, **kwargs):
        slack_message = request.data
        if not 'token' in slack_message:
            parse_message.delay(slack_message)
        return Response(status=status.HTTP_200_OK)
