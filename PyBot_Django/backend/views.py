from .train import chat

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(["POST"])
def sendResponse(request):
    msg = request.data["message"]
    ans = chat.get_response(msg)
    
    return Response(ans, status=status.HTTP_200_OK)